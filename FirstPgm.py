class Sample:
  
  def add(self,a=5,b=5,c):
      d=a+b+c
      print("add result=",d)
      
  def sub(self,a,b):
    c=a-b
    print("sub result=",c)
    
  def mul(self, a,b)
    c=a*b
    print("mul result=",c)
    
  def div(self, a=10,b=0)
  
    try:
      c=a/b
    expect zerodivisionError:
      print("skip the line')
            
  def m2(self):
      print('Praveen update m2 method')
            
 def m3(self):
      a,b,c=10,20,40
      d=a+b+c
      print("M3 result is",d)
      
s=Sample()
s.add(10,20,30)
s.sub(20,10)
s.mul(6,6)
s.div(10)
