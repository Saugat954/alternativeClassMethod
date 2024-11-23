class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary = salary
       
    def show(self):
        print(f"The name of employee is {self.name} and salary of employee is {self.salary}")

    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    
    
    
string = "Bijaya-80000"    

E1 = Employee("Saugat",10000)
E1.show()
print(E1.name,E1.salary)


E2 = Employee.fromstr(string)
E2.show()
print(E2.name,E2.salary)