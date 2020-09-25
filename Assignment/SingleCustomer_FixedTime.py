import simpy
from SimPy.Simulation import *                           


class Customer(Process):                                        
    def visit(self,timeInBank):                          
        print (now(),self.name," Here I am")               
        yield hold,self,timeInBank                       
        print (now(),self.name," I must leave")            


maxTime = 100.0     # minutes                            
timeInBank = 10.0   # minutes


initialize()                                             
c = Customer(name="Klaus")                               
activate(c,c.visit(timeInBank),at=5.0)                   
simulate(until=maxTime)           