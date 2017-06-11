import numpy as np

# arange
np.arange(6) #0から
array([0, 1, 2, 3, 4, 5]) 



# reshape
np.arange(6).reshape(3,2)

# linspace
np.linspace(0,1,4) 
 #array([ 0.        ,  0.33333333,  0.66666667,  1.        ])


# zeros_like
np.zeros_like([[1,2,3],[2,3,4]])

# ones_like
np.ones_like([[1,2,3],[2,3,4]])

# zeros
# np.zeros((3,2))
# array([[ 0.,  0.],
#        [ 0.,  0.],
#        [ 0.,  0.]])

# size
# 配列の要素数　を返す
 np.size([[1,2,3],[2,3,4]])

# flatten
# 多次元配列を一次元配列へ就職する
np.array([[1,2],[3,4],[5,6]]).flatten()

