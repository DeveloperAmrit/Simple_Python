
class programmer:
  company = "Microsoft"
  def __init__(self,name):
       self.name = name
       self.salary = "$ 200"
       self.product = "Printer"

  def getinfo(self):
      print("The name of the employee is ",self.name,".His salary is ",self.salary,"working for",self.company,self.product)

Alok = programmer("ALOk")

Alok.getinfo()