from abc import ABCMeta, abstarctmethod
#abstract base Class
#A base class which consists of abstract methods that should be implemented in its derived class is called an abstract base class.
'''#Syntax:
   from abc import ABCMeta, abstractmethod
   class baseClass(metaclass = ABCMeta):
   @abstractmethod
   def abstractMethod(self):
    return
'''   
#let's create a abstarct class
class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0


class Square(Shape):
    side = 4
    def area(self):
        print("Area of square:",self.side * self.side)

class Rectangle(Shape):
    width = 5
    length =10
    def area(self):
        print("Area of rectangle:",self.width*self.length)

square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
        