#init method is the first method that gets called


class Employee:

    def __init__(self):
        self.name ="Nitish"
   
    
    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee()
employee.displayEmployeeDetails()        