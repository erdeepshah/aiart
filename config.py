# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 23:34:52 2023

@author: deep.shah
"""

import torch

default = {
'checkpoint':'stabilityai/stable-diffusion-2-base', #'stabilityai/stable-diffusion-2'
'numInferenceSteps':35,
'port':5000,
'disableProgressBar':True,
'cudaDType':torch.float16,
'cudaRevision':'fp16',
'cpuDType':torch.float32,
'cpuRevision':'main',
'defaultSeed':342653748590041
}