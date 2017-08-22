#!/usr/bin/pyton3
#assign 100 to cars
cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car=passengers/cars_driven

#f is format string, so we are running python code inside a print statement 
print(f"There are {cars} cars available.")
print("There are only",drivers,"drivers available")
print("there will be",cars_not_driven,"empty cars today")
print("We can transport",carpool_capacity,"people today.")
print("We need to put about",average_passengers_per_car,"in each car.")

#assign 10 to types_of_people
types_of_people=10
#assign the string to xrange
x = f"There are {types_of_people} types of people."

binary ="binary"
do_not="don't"
y=f"Those who know{binary}are tose who {do_not}."

print(x)
print(y)

print(f"I said:{x}")
print(f"I also said:'{y}'")

hilarious=False
joke_evaluation="Isn't that joke so funny?!{}"

