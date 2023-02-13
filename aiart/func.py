# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 01:23:35 2023

@author: deep.shah
"""
import subprocess
import diffusers
import os
import time
import re
import requests
import atexit
import base64

def createPipe(checkpoint, torch_device, revision, torchDType):    
    #Construct
    pipe = diffusers.StableDiffusionPipeline.from_pretrained(checkpoint, revision=revision, torch_dtype=torchDType)
    pipe = pipe.to(torch_device)
    
    return pipe

def expose(port):   
    if 'p' in locals():
        p.kill()
    
    res1 = subprocess.run(["wget","-q","nc","https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"])
    os.chmod('./cloudflared-linux-amd64', 0o777)
    
    p = subprocess.Popen(['./cloudflared-linux-amd64', 'tunnel', '--url', 'http://127.0.0.1:' + str(port), '--metrics', '127.0.0.1:8099'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    atexit.register(p.terminate)
    localhost_url = "http://127.0.0.1:8099/metrics"
    attempts = 0
    while attempts < 10:
        try:
            tunnel_url = requests.get(localhost_url).text
            tunnel_url = (re.search("(?P<url>https?:\/\/[^\s]+.trycloudflare.com)", tunnel_url).group("url"))
            break
        except:
            attempts += 1
            time.sleep(3)
            continue
    if attempts == 10:
        raise Exception("Can't connect to Cloudflare Edge")
    
    eurl = base64.b64encode(tunnel_url.encode('utf-8').hex().encode('utf-8')).decode('ascii')
    
    return eurl
