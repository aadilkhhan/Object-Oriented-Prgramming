class Employee:
    company = "Google"


    def __init__(self , name , salary , subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetalis(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")


    def getSalary(self , signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good morning , Sir")

    @staticmethod
    def time():
        print("The time is 9am in the morning")

Aadil = Employee("Aadil" , 100 , "Youtube")
# Aadil = Employee() ---> # Throws an error (missing 3 required positional arguments)
Aadil.getDetalis()

