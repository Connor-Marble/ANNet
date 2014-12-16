import math
from collections import namedtuple

Connection = namedtuple('Connection', 'neuron, weight')

Activation_Threshhold = -0.5

class Neuron():
    output = 0
    connections = []
    
    def __init__(self, prevlayer, startweight):
        for i in prevlayer:
            self.addconnection(i, startweight)

    def evaluate(self):
                 
        inputsum = sum(i.neuron.output * (i.weight) for i in self.connections)
        self.output = self.neuralfunction(inputsum+Activation_Threshhold)
        return (inputsum, self.output)
        
    def neuralfunction(self, inputsum):
        #logistic sigmoid
        return 1/(1 + math.exp(-inputsum))
        
    def getvalue(self):
        return self.output

    def addconnection(self, connected, weight):
        self.connections.append(Connection(connected, weight))

    def __str__(self):
        return str(self.output)

    
