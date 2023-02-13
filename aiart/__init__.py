# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 01:23:35 2023

@author: deep.shah
"""

from aiart.func import createPipe
from aiart.func import expose

from flask import Flask
import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True

import aiart.routes