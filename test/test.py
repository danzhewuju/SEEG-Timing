#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 20:20
# @Author  : Alex
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# from data.generatedata import generate_data
import numpy as np
from collections import Counter
import pandas as pd
import uuid
import re
import random
import torch
from torch import nn
import torch.nn.functional as F
import torch.nn.utils.rnn as rnn_utils

if __name__ == '__main__':
    a = torch.rand(1, 3, 10)
    print(a)
    # b = F.pad(a, (0, 6000, 0, 0, 0, 0), 'constant')
    b = np.pad(a, ((0, 0), (0, 0), (0, 6000)), 'constant')
    print(b.shape)
