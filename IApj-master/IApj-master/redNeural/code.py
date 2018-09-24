import neurolab as nl
import numpy as np
import pylab as pl

def NN_for_234_hidden_node():
    '''
    Train a neural net work for one hiden layer and 2, 3, 4 hidden nodes,
    then plot and compare sum of squared error for different design
    '''

    inputs = np.eye(3) # Create the input and target
    inp = inputs[2] # input used to test the neural network
    inp = inp.reshape(1,3) # transform inp from one row to 8 row 1 column
    #inputs = np.delete(inputs , 5, 0) # delete 0000 0100
    print(inputs)
    error = []
 # node_number denote the number of nodes in hiden layer.
    for node_number in range(2, 4 + 1):
        # [[0, 1]] * 8 denote that there EIGHT input nodes and the range of each input is from 0 to 1
        # [node_number, 7] denote that the hidden layer contains "node_number" neurons and have 8 out put.
  # transf=[nl.trans.LogSig()] * 2 shows that using Log Signoid function in nodes.
        net = nl.net.newff([[0, 1]] * 8, [node_number, 8], transf=[nl.trans.LogSig()] * 2)  # @UndefinedVariable
        # net = nl.net.newff([[0, 1]] * 8, [node_number, 8])  # @UndefinedVariable
  # using Resilient Backpropagation to train the network.
  # This is the best way to train in this example in all provided Backpropagation algorithm
        net.trainf = nl.train.train_rprop  # @UndefinedVariable
        # default transfer function for newff is tan sigmoid

        # net = nl.net.newp([[0, 1]]*8, 2)  # @UndefinedVariable

  # train network and generate errors. the default method to generate error is Sum of Squared Error
        error.append(net.train(inputs, inputs, show=0, epochs = 3000))  # @UndefinedVariable
        print("The input array is: ", inp)
        out = net.sim(inp) # compute output for input "inp"
        print(out)

  # this small block of code used to compare network result with expected result.
#         pl.plot(range(8), inp[0])
#         pl.plot(range(8), out[0])
#         pl.show()
#         print(out)
#         print(net.layers[0].np)
        sigmoid = nl.trans.LogSig();  # @UndefinedVariable

  # compute the value of nodes in each hidden layer
        for inputs_idx in range(len(inputs)):
            result = []
            for perce_idx in range(node_number):
                result.append(sigmoid((net.layers[0].np['w'][perce_idx] * inputs[inputs_idx]).sum()
                                      + (net.layers[0].np['b'][perce_idx])))
            print("For the ", inputs_idx, " The value of each node is: ")
            print(result)

    # plot the error of 3 different network
    for i in range(len(error)):
        label_str = str(i + 2) + " nodes"
        # label_str = str(label_str)
        # print(str(label_str))
        pl.plot(range(len(error[i])), error[i], label=label_str)
    pl.legend()
    pl.xlabel("number of iteration")
    pl.ylabel("sum of squared error")
    pl.title("Sum of squared error for NN with different hidden nodes")
    pl.show()

NN_for_234_hidden_node()
