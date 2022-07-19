class Sample:
  
  def add(self,a=5,b=5,c):
      d=a+b+c
      print("add result=",d)
      
  def sub(self,a,b):
    c=a-b
    print("sub result=",c)
      
s=Sample()
s.add(10,20,30)
s.sub()
