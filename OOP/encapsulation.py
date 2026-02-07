class Stud:
    def __init__(self):
        self.__name=None
        self.__marks=None

        

    def get__name(self):
        return self.__name
    
    def set__name(self,new_name):
        self.__name=new_name

    def get__marks(self):
        return self.__marks

    def set__marks(self,new_marks):
        self.__marks=new_marks

s=Stud()
s.set__name("Sujal")    
s.set__marks(60)

print(s.get__name())
print(s.get__marks())

     