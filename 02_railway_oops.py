class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

AadilsApplication = RailwayForm()
AadilsApplication.name = "Aadil"
AadilsApplication.train = "Betwa Express"
AadilsApplication.printData()