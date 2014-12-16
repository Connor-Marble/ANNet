from Neuron import *
from random import uniform

class NeuralNetwork():
    layers = []
    
    def __init__(self, layer_count):
        for i in layer_count:
            self.addlayer(i)

    def addlayer(self, size):
        layer = []
        for i in range(size):
            if len(self.layers) > 0:
                layer.append(Neuron(self.layers[len(self.layers)-1],0))
            else:
                layer.append(Neuron([],0))

        self.layers.append(layer)

    def setinput(self, inputs):
        for i in range(len(inputs)):
            self.layers[0][i].output = inputs[i]
            
    def __str__(self):
        printstr = ''
        for i in self.layers:
            layer = ''
            for j in i:
                layer += str(j)+' '
            printstr+=layer + '\n'
        return printstr

    def evaluate(self):
        for layer in self.layers:
            for neuron in layer:
                neuron.evaluate()

if __name__=='__main__':
    net = NeuralNetwork([3,5,6,5,4])
    net.setinput([0,0.9,0.1])
    net.evaluate()
    print(net)
                    
                
