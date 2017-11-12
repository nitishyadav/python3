class Employee:
    name ="Nitish"
    designation = "Cloud Automation Engineer"
    workedThisWeek = 45
    def hasAchievedTarget(self):
        if self.workedThisWeek >=40:
            print("Target achieved")
        else:
            print("target missed")
        
employee1 = Employee()
employee2 = Employee()            
employee1.hasAchievedTarget()
print(employee1.name)