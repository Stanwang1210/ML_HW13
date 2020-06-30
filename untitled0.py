### -*- coding: utf-8 -*-
##"""
##Created on Sat Jun 27 20:46:19 2020
##
##@author: 王式珩
##"""
##
##
##from torch.distributions import Categorical
##import torch
##from tqdm import tqdm_notebook
##import time
###x = torch.rand(1, 4)
###print(x)
###m = Categorical(x)
###m.sample()
###probs = torch.Tensor([ [0.1, 0.2, 0.7], [0.1, 0.8, 0.1], [0.0, 0.0, 1.0] ])
###prob_dist = torch.distributions.Categorical(probs) # probs should be of size batch x classes
###prob_dist.sample()
##NUM_BATCH = 100
##prg_bar = tqdm_notebook(range(NUM_BATCH))
##for x  in prg_bar:
##    print(x)
##    time.sleep(0.1)
#
#from tqdm import trange
#from time import sleep
#
#for i in trange(10, desc='1st loop'):
#    for j in trange(5, desc='2nd loop', leave=False):
#        for k in trange(100, desc='3nd loop'):
#            sleep(0.01)
import numpy as np

x = np.full(3, 2)
b = [x]
a = np.concatenate(b, axis = 0)
print(a)



