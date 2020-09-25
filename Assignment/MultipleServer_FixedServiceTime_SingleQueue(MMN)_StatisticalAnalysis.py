from SimPy.Simulation import * 
from random import expovariate,seed


class Source(Process):
    def generate(self,number,interval,resource,mon):       
        for i in range(number):
            c = Customer(name = "Customer%02d"%(i,))
            activate(c,c.visit(b=resource,M=mon))          
            t = interval
            yield hold,self,t

class Customer(Process):
    def visit(self,b,M):       
        arrive = now()
        yield request,self,b
        wait = now()-arrive
        M.observe(wait)                                
        tib = timeInBank
        yield hold,self,tib
        yield release,self,b


maxNumber = 20
maxTime = 2000.0  # minutes                                    
timeInBank = 21.0   # mean, minutes
ARRint = 10.0     # mean, minutes
Nc = 2            # number of counters


def model():                            
    k = Resource(capacity=Nc,name="Clerk")  
    wM = Monitor()                                   

    initialize()
    s = Source('Source')
    activate(s,s.generate(number=maxNumber,interval=ARRint,resource=k,mon=wM),at=0.0)         
    simulate(until=maxTime)
    return (wM.mean(), wM.total())                     


theseeds = [393939,31555999,777999555,319999771]         
for Sd in theseeds:
    result = model()
    print ("Average waiting time %5.2f minutes. Total %5.2f"% result  )
