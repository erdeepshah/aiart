# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 01:23:35 2023

@author: deep.shah
"""

import torch
import diffusers
import func
from flask import Flask, send_file, request
import io
import config as cfg

#configs
torch.backends.cudnn.benchmark = True

checkpoint = cfg.default['checkpoint']
num_inference_steps = cfg.default['numInferenceSteps']
port = cfg.default['port']
if(cfg.default['disableProgressBar'] == True):
    diffusers.logging.disable_progress_bar()

torch_device = "cuda" if torch.cuda.is_available() else "cpu"
if(torch_device == "cuda"):
    torchDType = cfg.default['cudaDType']
    revision = cfg.default['cudaRevision']
else:
    torchDType = cfg.default['cpuDType']
    revision = cfg.default['cpuRevision']

pipe = func.createPipe(checkpoint, torch_device, revision, torchDType)

# #Server
# app = Flask(__name__)

@app.route("/")
def home():
    return "AI Art index api"

@app.route("/gen", methods=['post'])
def gen():
    prompt = request.form.get('prompt')
    try:
      seed = int(request.form.get('seed'))
    except:
      seed = cfg.default['seed']

    #prompt = 'sun dancing with moon'
    generator = torch.Generator(torch_device).manual_seed(seed)
    image = pipe(prompt, num_inference_steps=num_inference_steps, generator=generator).images[0]

    img_io = io.BytesIO()
    image.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')