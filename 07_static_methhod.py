class Employee:
    company = "Google"
    def getSalary(self , signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good morning , Sir")

    @staticmethod
    def time():
        print("The time is 9am in the morning")

Aadil = Employee()
Aadil.salary = 100000
Aadil.getSalary("Thanks") # Employee.getSalary(Aadil)
Aadil.greet() #Employee.greet()
Aadil.time()
