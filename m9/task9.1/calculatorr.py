class Calculator:
 def add(self, a, b):
   return a+b
 def subtract(self, a, b):
   return a-b
 def multiply(self, a, b):
   return a*b
 def divide(self, a, b):
     if isinstance(a,int) and isinstance(b, int):

         return a/b
     else:
         return "ERROR"

res=Calculator()

#print(res.add(10,2))
#print(res.subtract(10,2))
#print(res.multiply(10,2))
#print(res.divide(10,2))
