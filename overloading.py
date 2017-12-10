#here we are using polymorphism and method overloading

class Square:
    def __init__(self, side):
        self.side = side

    # Overload the exponential operator
    def __pow__(squareOne, squareTwo):
        # Return side of squareOne to the power of side of squareTwo
        return squareOne.side ** squareTwo.side

squareOne = Square(2)
squareTwo = Square(4)
print("squareOne to the power of squareTwo = ", squareOne ** squareTwo)
