from pybrain.tools.shortcuts import buildNetwork

#Dos capas de entrada, tres intermedias y una de salida
net = buildNetwork(2, 3, 1)

#Activar con valores random
net.activate([2,1])

#Dos entradas una salida
ds = SupervisedDataSet(2, 1)

ds.addSample((0, 0), (0,))
ds.addSample((0, 1), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 1), (0,))

for inpt, target in ds:
    print (inpt, target)
