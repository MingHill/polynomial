class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, xval): 
        return xval
    

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, xval): 
        return self.i; 

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, xval): 
        return self.p1.evaluate(xval) + self.p2.evaluate(xval)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            repr1 = "( " + repr(self.p1) + " )"
        else: 
            repr1 = repr(self.p1)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            repr2 = "( " + repr(self.p2) + " )"
        else: 
            repr2 = repr(self.p2)
        return repr1 + " * " + repr2
    
    def evaluate(self, xval): 
        return self.p1.evaluate(xval) * self.p2.evaluate(xval)

class Div: 
    def __init__(self, p1, p2): 
        self.p1 = p1
        self.p2 = p2 
    
    def __repr__(self): 
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            repr1 = "( " + repr(self.p1) + " )"
        else: 
            repr1 = repr(self.p1)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            repr2 = "( " + repr(self.p2) + " )"
        else: 
            repr2 = repr(self.p2)
        return repr1 + " / " + repr2

    def evaluate(self, xval): 
        return self.p1.evaluate(xval) / self.p2.evaluate(xval)
    
    
    
class Sub: 
    def __init__(self, p1, p2): 
        self.p1 = p1 
        self.p2 = p2 
    
    def __repr__(self): 
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, xval): 
        return self.p1.evaluate(xval) - self.p2.evaluate(xval)
    
    
    


#poly = Sub(Int(10), X())
poly2 = Sub(Div(Add(Int(2), Int(5)), Int(10)), Sub(Add(Int(3), X()), Int(23)))
print(poly2)
print(poly2.evaluate(30))
# print(poly2)