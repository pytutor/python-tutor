from numpy import *
# creating the data and time steps
time = linspace(20, 145, 5)
data = sin(arange(20)).reshape(5,4)

ind = data.argmax(axis=0)
time_max = time[ ind]
data_max = data[ind, xrange(data.shape[1])]
