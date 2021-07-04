
class Employee:
    company = "Google"
    salary = 100

aadil = Employee()
diksha = Employee()

# Creating instance attribute salary for both the objects
# aadil.salary = 300
# diksha.salary = 400
aadil.salary = 45

print(aadil.salary)
print(diksha.salary)

# Below line throws an error as addres is not present in instance/class
# print(aadil.address)