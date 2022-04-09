#  Unlimited Positional Arguments
# CHALLENGE #1: Write a function that can takes as many numbers as we want.
#  Then it will return sum of all the numbers.
def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(add(5, 9, 2, 88, 45, 90))
# OUTPUT: 239


#  Unlimited Keyword Arguments
def calculate(num, **kwargs):
    print(kwargs)  # OUTPUT: {'add': 3, 'multiply': 9}
    for key,value in kwargs.items():
        print(key)  # OUTPUT: 'add', 'multiply'
        print(value)  # OUTPUT: 3, 9
    print(kwargs["add"])  # OUTPUT: 3
    num += kwargs["add"]  # 4 + 3 = 7
    num += kwargs["multiply"]  # 7 + 9 = 16
    print(num)  # OUTPUT: 16


calculate(4, add=3, multiply=9)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]  # We have to give this argument, otherwise it will show an error.
        self.model = kwargs.get("model")  # If we use .get method, we can leave this arguments.


my_car = Car(make="Nissan", model="Sonata")
print(my_car.make)  # OUTPUT: Nissan
print(my_car.model)  # OUTPUT: Sonata