class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")


Aadil = Employee()
Aadil.salary = 100000
Aadil.getSalary() # Employee.getSalary(Aadil)