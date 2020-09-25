from SimPy.Simulation import *


class Source(Process):                              
    def generate(self,number,TBA):                  
        for i in range(number):
            c = Customer(name = "Customer%02d"%(i,))
            activate(c,c.visit(timeInBank=12.0))
            yield hold,self,TBA                     

class Customer(Process):       
    def visit(self,timeInBank):       
        print ("%7.4f %s: Here I am"%(now(),self.name))
        yield hold,self,timeInBank
        print ("%7.4f %s: I must leave"%(now(),self.name))


maxNumber = 5
maxTime = 400.0 # minutes                                    
ARRint = 10.0   # time between arrivals, minutes 


initialize()
s = Source()                                             
activate(s,s.generate(number=maxNumber,TBA=ARRint),at=0.0)             
simulate(until=maxTime)