
class Employee:
    company = "Google"
    salary = 100

aadil = Employee()
diksha = Employee()

aadil.salary = 300
diksha.salary = 400

print(aadil.company)
print(diksha.company)
Employee.company = "You tube"
print(aadil.company)
print(diksha.company)
print(aadil.salary)
print(diksha.salary)
