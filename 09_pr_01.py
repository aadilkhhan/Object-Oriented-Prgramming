class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(
            f"The name of the pragrammer is {self.name} and the product is {self.product}")


aadil = Programmer("Aadil", "skype")
jethuram = Programmer("Jethuram", "Github")
aadil.getInfo()
jethuram.getInfo()