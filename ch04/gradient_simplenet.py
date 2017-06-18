# coding: utf-8
import sys, os
sys.path.append(os.pardir) 
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient
import numpy as np

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)
    
    def predict(self, x):
        return np.dot(x, self.W)
    
    def loss(self, x, t):
        # print(self)
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        
        return loss

