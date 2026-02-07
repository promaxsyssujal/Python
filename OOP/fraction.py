class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d

        self.operation()
        
    def operation(self):
        result=self.num/self.den
        print("Result>>",result)

s=Fraction(4,5)