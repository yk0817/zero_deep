
# coding: utf-8

# In[ ]:




# In[6]:


import sys, os
sys.path.append(os.pardir) 
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient
from gradient_simplenet import simpleNet
import numpy as np
net = simpleNet()

# print(net.W)
x = np.array([0.6,0.9])
p = net.predict(x)
# print(p)
# np.argmax(p)
t = np.array([0,0,1])
net.loss(x,t)


def f(W):
    return net.loss(x,t)

dW = numerical_gradient(f, net.W)
# print(dW)



# In[ ]:



