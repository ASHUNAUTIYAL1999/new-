class house:
    def __init__(self,name ,age,address,salary):
        self.name=name
        self.age=age
        self._address=address
        self.__salary=salary

    def get_salary(self):
        print(self.__salary)
    
    def detail(self):
        print(self.name,self.age)

    def places(self):
        print(self._address)

c1=house("ashu",23,"guna",60000)
print(c1._address)
c1.detail()
c1.places()
c1.get_salary()
print(c1.age)
print(c1.__salary)
