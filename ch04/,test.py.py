
# coding: utf-8

# In[7]:


import sys, os
sys.path.append(os.pardir) 
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient
from gradient_simplenet import simpleNet

net = simpleNet()


# In[ ]:



