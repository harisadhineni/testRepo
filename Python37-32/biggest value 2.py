# single inheritance

class parent:
    a = 0
    b = 0
    c = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add (self):
        self.c = self.a +self.b
        print('the result is parent class:',self.c)
class child(parent):
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def display(self):
        e1 = parent(self.x,self.y)
        e1.add()
e2 = child(4,5)
e2.display()
        
        
                            

    

    
