<<<<<<< HEAD
#from _typeshed import Self
#from _typeshed import Self
import math
import random as R
from re import L
import numpy as np
class layer:
    def __init__(self,size,pre_Layer=[]) -> None:
        self.pre_layer=pre_Layer
        self.size=size
        self.newrons=[]
        for x in range(size):          
           self.newrons.append(len(pre_Layer))
    def feed_forward(self):
        output_layer=[]
        for x in self.newrons:
            output_layer.append(x.output_value(self.pre_layer))
        return output_layer
    class newron:
        #return 1/(1+e^-x)
        def defult_out_function(x):
            return 1/(1+math.exp(-x))
        def __init_subclass__(cls,n,f=defult_out_function) -> None:
            cls.byte=R.randint(-100,100)
            cls.size=n
            cls.wights=[]
            for i in range(n):
                cls.wights.append(R.random())
            cls.output_function=f
            cls.output_val=0
        def output_value(cls,inputs):
            output=0
            for i in range(cls.n):
                output+=cls.wights[i] * inputs[i]
            output+=cls.byte
            cls.output_val=output
            return cls.output_function(output)
        def Backpropagation(cls,exepted_result):
            error=exepted_result-cls.output_val
            for wight in cls.wights:
                wight-=error*(wight/sum(wight))
def main(inputs=[]):  
   network=[]
   n=input("Please enter the number of layers you want:")
   try:
       n=int(n)
   except:
        print("wrong output. You must enter an intager bigger then zero.")
   if(type(n) != int or n<=0):
       print("wrong output. You must enter an intager bigger then zero.")
       exit(1)
   if(not(inputs)):
      size=input("Enter the size of the input layer")
      for i in range(size):
        try:
         inputs.append(float(input(str.format("Enter number in index {}",i))))
        except:
            print("You must enter a float number.")
            inputs.append(float(input(str.format("Enter number in index {}",i))))
   print("In the first layer the size by defult is the size of the input.")
   prelayer=inputs
   for i in range(1,n):
      p=input(str.format("Please enter the number of neurons in layer number {} .",i))
      l=layer(p,prelayer)
      network.append(l)
      prelayer=l

   for i in range(0,):
      for j in range(n):
          network[j].feed_forward()
        






        
=======
#from _typeshed import Self
import math
import random as R
import numpy as np
class layer:
    def __init__(self,func,weights,params):
        self.params=params
        self.Activationfunc=func
        self.weights=weights
        self.bies=0
    def OutputValue(self):
        return self.Activationfunc(self.sigma())
    def sigma(self):
        Sum=self.bies
        for i in (0,len(self.params)):
           Sum+=self.params[i]*self.weights[i]
        return sum
    
    


class network:
   def __init__(self,Layerarchitecture,outputs,inputs) :
       self.weights=[]
       Layerarchitecture.insert(0,len(inputs))
       Layerarchitecture.append(len(inputs))
      # for x in input:
      #   weights.append(random.random())
       self.data=[]
       self.data.append(inputs)      
       self.NOL=len(Layerarchitecture)
       for i in range(0,self.NOL):
          self.weights.append([R.random() for j in range(0,Layerarchitecture[i])])
          self.data.insert(i+1,[0 for j in range(0,Layerarchitecture[i])])   
       self.data.append(outputs)
       self.bays=[0 for i in range(self.NOL)]
       self.architecture=Layerarchitecture
   def ramp(self,x):
       if(x>=0):return 1
       else:return 0


   def Activationfunction(self,x,i):
       return{
           0:x,
           1:1/(1-math.exp(-x)),
           2:self.ramp(x),
           3: math.tanh(x),
           4:math.ln(1+math.exp(x))
       }.get(i,x)

   def feedforward(self):     
     for x in range(self.NOL):
      temp=[]
      for z in range(self.architecture[x]):    
       some=[]
       a=R.randint(3,10) 
       for y in range(a):        
         r=R.randint(0,self.architecture[x]-1)
         some.append(self.data[x][r]*self.weights[x][r])
       temp.append(sum(some)+self.bays[x])
      self.data[x+1]=temp
      print(self.data)
      

       
        
     
if __name__ == "__main__":
   net=network([2],[2,3],[1,2])
   net.feedforward()


               
           

       
           

       

        


>>>>>>> 0f28a2f (null)
