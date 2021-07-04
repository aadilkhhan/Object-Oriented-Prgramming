class Sample:
    def __init__(slf , name):
        slf.name = name
# Yes we can change the self parameter inside the function and class

obj = Sample("Aadil")
print(obj.name)

