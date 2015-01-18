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
                layer.append(Neuron(self.layers[len(self.layers)-1],uniform(-0.5,0.5)))
            else:
                layer.append(Neuron([],uniform(-0.5,0.5)))

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

    def backpropogate(self, targetoutput):
        error = []
        error.append(self.get_output_error(targetoutput))
        for layer in reversed(self.layers[1:-1]):
            newerrorlayer = [neuron.geterror(error[0]) for neuron in layer]
            error.insert(0, newerrorlayer)
        print error
        
        
    def get_output_error(self, targetoutput):
        outputvalues = [x.output for x in self.layers[-1]]
        return map(lambda a,b: a-b,targetoutput, outputvalues)
        
if __name__=='__main__':
    net = NeuralNetwork([3,5,6,5,4])
    net.setinput([0,0.9,0.1])
    net.evaluate()
    print net
    print 'error:'
    net.backpropogate(range(4))
    
                    
                
