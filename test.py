import numpy as np

def convolution(arr1, arr2):
    arr1 = np.pad(arr1, ((1,1), (1,1)), 'constant')
    print(arr1)
    h1, w1 = arr1.shape
    h2, w2 = arr2.shape
    rh = h1 - h2 + 1
    rw = w1 - w2 + 1
    
    res = np.zeros([rh, rw])
    
    for y in range(rh):
        for x in range(rw):
            res[y][x] = np.inner(arr1[y:y+w2,x:x+h2].flatten(), filter.flatten())

    return res

img = np.ones((28,28))
filter = np.array([[1,0,1],
                   [0,1,0],
                   [1,0,1]])

res = convolution(img, filter)
print(res.shape)
