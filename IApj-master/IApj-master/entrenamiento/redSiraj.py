# coding: utf-8

# # Annotations for the Sirajology Python NN Example
#
# This code comes from a demo NN program from the YouTube video https://youtu.be/h3l4qz76JhQ. The program creates an neural network that simulates the exclusive OR function with two inputs and one output.
#
#

# In[23]:

import numpy as np  # Note: there is a typo on this line in the video

import matplotlib.pyplot as pl
# The following is a function definition of the sigmoid function, which is the type of non-linearity chosen for this neural net. It is not the only type of non-linearity that can be chosen, but is has nice analytical features and is easy to teach with. In practice, large-scale deep learning systems use piecewise-linear functions because they are much less expensive to evaluate.
#
# The implementation of this function does double duty. If the deriv=True flag is passed in, the function instead calculates the derivative of the function, which is used in the error backpropogation step.

# In[24]:

def nonlin(x, deriv=False):  # Note: there is a typo on this line in the video
    if(deriv==True):
        return (x*(1-x))

    return 1/(1+np.exp(-x))  # Note: there is a typo on this line in the video



np.set_printoptions(suppress=True)
# The following code creates the input matrix. Although not mentioned in the video, the third column is for accommodating the bias term and is not part of the input.

# In[25]:

#input data
X = np.array([[0,0,1],  # Note: there is a typo on this line in the video
            [0,1,1],
            [1,0,1],
            [1,1,1]])

X = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 92.94],
            [0.0, 0.0, 54.61, 0.0, 0.06, 42.39, 0.0, 1.96],
            [0.0, 0.0, 16.1, 0.0, 0.0, 1.43, 3.31, 79.16],
            [0.0, 0.0, 31.33, 0.0, 0.0, 0.0, 6.04, 62.37],
            [0.0, 0.0, 28.78, 0.0, 0.0, 0.65, 28.55, 41.94],
            [0.0, 0.0, 24.24, 1.22, 0.0, 70.18, 0.45, 3.9],
            [0.0, 0.0, 14.73, 0.0, 0.0, 3.78, 3.1, 78.18],
            [0.0, 0.0, 0.37, 0.0, 0.0, 84.61, 8.24, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 3.45, 0.0, 55.63],
            [0.0, 0.0, 0.57, 0.0, 0.0, 84.06, 12.98, 0.0],
            [1.06, 0.0, 14.37, 0.0, 0.0, 5.47, 38.82, 35.45],
            [0.0, 0.0, 40.86, 0.02, 0.0, 54.86, 2.88, 0.94],
            [0.0, 0.0, 17.33, 0.0, 0.0, 51.41, 12.29, 12.27],
            [0.0, 0.0, 24.1, 0.14, 0.0, 69.73, 0.08, 4.49],
            [0.0, 0.0, 8.63, 0.0, 0.0, 0.0, 0.0, 91.29],
            [0.0, 0.0, 42.67, 0.0, 0.0, 0.0, 2.67, 54.65],
            [0.0, 0.0, 48.57, 0.0, 0.0, 26.12, 0.27, 13.02],
            [0.0, 0.0, 54.73, 0.0, 0.0, 0.0, 0.0, 45.27],
            [0.0, 0.0, 8.61, 0.0, 0.0, 67.76, 18.35, 5.29],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 98.47],
            [0.0, 0.0, 60.02, 0.0, 0.0, 34.41, 4.49, 0.63],
            [0.0, 0.0, 21.29, 0.0, 0.0, 12.94, 63.12, 2.59],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.18, 0.0, 86.35],
            [0.0, 0.0, 22.24, 0.0, 0.0, 44.94, 16.71, 13.96],
            [0.0, 0.0, 0.16, 0.0, 0.0, 68.86, 7.59, 0.0],
            [0.0, 0.0, 50.51, 0.0, 0.22, 44.12, 0.0, 1.96],
            [0.0, 0.0, 35.31, 0.43, 0.0, 61.33, 0.92, 1.55],
            [0.76, 0.0, 0.08, 0.0, 3.0, 26.61, 0.73, 40.78],
            [0.0, 0.0, 1.86, 0.0, 0.0, 1.88, 0.02, 87.86],
            [0.0, 0.0, 10.92, 0.0, 0.0, 41.94, 11.47, 35.65],
            [0.0, 0.0, 4.8, 0.0, 0.0, 0.0, 0.0, 95.02],
            [0.0, 0.0, 38.18, 0.0, 0.0, 58.69, 2.02, 0.63],
            [0.55, 0.0, 0.02, 0.0, 3.02, 29.1, 0.65, 37.41],
            [0.0, 0.0, 10.06, 0.0, 0.0, 0.0, 85.41, 4.53],
            [0.0, 0.0, 1.78, 0.0, 0.0, 79.86, 17.27, 0.43],
            [0.0, 0.0, 14.06, 0.0, 0.0, 1.61, 1.73, 81.02],
            [0.0, 0.0, 22.14, 0.04, 0.0, 72.57, 3.92, 1.29],
            [0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 33.33],
            [0.0, 0.0, 52.86, 0.0, 0.0, 47.14, 0.0, 0.0],
            [0.0, 0.0, 86.24, 0.0, 0.0, 0.0, 0.0, 13.76],
            [0.0, 0.0, 25.29, 0.0, 0.0, 40.49, 20.14, 12.61],
            [0.0, 0.0, 27.69, 0.0, 0.59, 65.8, 0.0, 0.73],
            [0.0, 0.0, 31.33, 0.0, 0.0, 5.22, 39.14, 24.16],
            [0.0, 0.0, 22.8, 0.0, 0.0, 46.94, 0.1, 12.45]])

# The output of the exclusive OR function follows.

# In[26]:

#output data

y = np.array([[0,0,0,0,0,1],
            [1,0,0,0,0,0],
            [0,0,0,0,0,1],
            [0,0,0,0,1,0],
            [0,0,0,1,0,0],
            [1,0,0,0,0,0],
            [0,0,0,0,0,1],
            [0,0,1,0,0,0],
            [0,0,0,0,0,1],
            [0,0,1,0,0,0],
            [0,0,0,0,0,1],
            [1,0,0,0,0,0],
            [0,0,0,1,0,0],
            [0,1,0,0,0,0],
            [0,0,0,0,0,1],
            [0,0,0,0,1,0],
            [1,0,0,0,0,0],
            [0,0,0,1,0,0],
            [0,0,1,0,0,0],
            [0,0,0,0,0,1],
            [1,0,0,0,0,0],
            [0,0,0,1,0,0],
            [0,0,0,0,0,1],
            [0,0,0,0,1,0],
            [0,0,1,0,0,0],
            [1,0,0,0,0,0],
            [1,0,0,0,0,0],
            [0,0,0,0,0,1],
            [0,0,0,0,0,1],
            [0,0,0,0,1,0],
            [0,0,0,0,0,1],
            [1,0,0,0,0,0],
            [0,0,0,0,0,1],
            [0,0,0,1,0,0],
            [0,0,1,0,0,0],
            [0,0,0,0,0,1],
            [1,0,0,0,0,0],
            [0,0,0,0,0,1],
            [1,0,0,0,0,0],
            [0,0,0,0,1,0],
            [0,0,0,1,0,0],
            [1,0,0,0,0,0],
            [0,0,0,1,0,0],
            [0,0,0,1,0,0]])


erroresSum = []

# The seed for the random generator is set so that it will return the same random numbers each time, which is sometimes useful for debugging.

# In[27]:

np.random.seed(1)


# Now we intialize the weights to random values. syn0 are the weights between the input layer and the hidden layer.  It is a 3x4 matrix because there are two input weights plus a bias term (=3) and four nodes in the hidden layer (=4). syn1 are the weights between the hidden layer and the output layer. It is a 4x1 matrix because there are 4 nodes in the hidden layer and one output. Note that there is no bias term feeding the output layer in this example. The weights are initially generated randomly because optimization tends not to work well when all the weights start at the same value. Note that neither of the neural networks shown in the video describe the example.

# In[28]:

#synapses
syn0 = 2*np.random.random((8,44)) - 1  # 3x4 matrix of weights ((2 inputs + 1 bias) x 4 nodes in the hidden layer)
syn1 = 2*np.random.random((44,6)) - 1  # 4x1 matrix of weights. (4 nodes x 1 output) - no bias term in the hidden layer.


# This is the main training loop. The output shows the evolution of the error between the model and desired. The error steadily decreases.

# In[29]:

#training step
# Python2 Note: In the follow command, you may improve
#   performance by replacing 'range' with 'xrange'.
for j in range(600000):

    # Calculate forward through the network.
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    # Back propagation of errors using the chain rule.
    l2_error = y - l2

    if(j % 10000) == 0:   # Only print the error every 10000 steps, to save time and limit the amount of output.

        print("Error: " + str(np.mean(np.abs(l2_error))))

    #if (j % 150) == 0:
    erroresSum.append(np.mean(np.abs(l2_error)))


    l2_delta = l2_error*nonlin(l2, deriv=True)

    l1_error = l2_delta.dot(syn1.T)

    l1_delta = l1_error * nonlin(l1,deriv=True)

    #update weights (no learning rate term)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print("Output after training")
print(l2)
print ("\n\n\n Syn0: \n")
print (syn0)
print ("\n\n\n Syn1: \n")
print (syn1)

#
# pl.axhline(0, color="black")
# pl.axvline(0, color="black")
# pl.plot(np.arange(0., len(erroresSum), 100.),np.array(erroresSum))
# pl.grid(True)
# pl.show()
print (len(erroresSum))
print("Error: " + str(np.mean(np.abs(l2_error))))

pl.axhline(0, color="black")
pl.axvline(0, color="black")
pl.plot(np.arange(0., len(erroresSum), 1.),np.array(erroresSum))
pl.grid(True)
pl.show()
