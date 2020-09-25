from SimPy.Simulation import *
from random import expovariate, seed


class Source(Process):
    def generate(self,number,meanTBA,resource):      
        for i in range(number):
            c = Customer(name = "Job%02d"%(i,))
            activate(c,c.visit(b=resource))            
            t = meanTBA
            yield hold,self,t

class Customer(Process):
    def visit(self,b):                                
        arrive = now()
        print ("%8.4f %s: Here I am     "%(now(),self.name))
        yield request,self,b                          
        wait = now()-arrive
        print ("%8.4f %s: Waited %6.3f"%(now(),self.name,wait))
        tib = timeInBank
        yield hold,self,tib                          
        yield release,self,b                         
        print ("%8.4f %s: Finished      "%(now(),self.name))


maxNumber = 20
maxTime = 400.0 # minutes                                      
timeInBank = 12.0 # minutes                      
ARRint = 12.0   # minutes                      
theseed = 12345                                        


seed(theseed)                                        
k = Resource(capacity=2,name="Counter",unitName="Clerk")  

initialize()
s = Source('Source')
activate(s, s.generate(number=maxNumber,meanTBA=ARRint,resource=k),at=0.0)           
simulate(until=maxTime)