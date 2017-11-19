#Example of multiple inheritence

class OperatingSystem:
    multitasking = True
    Name = "Mac OS"
    
class Apple:
    website = "www.apple.com"
    Name = "Apple"

class Macbook(OperatingSystem,Apple):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multi tasking system. Visit {} for motr details".format(self.website))
            #same attribute name, then output depends on order of inheritence
            print("Name:",self.Name)

macBook = Macbook()            