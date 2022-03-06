# import imp
# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column(
    "Country",
    [
        "Bangladesh",
        "United State of America", 
        "England", 
        "Germany"
    ]
)
table.add_column(
    "City",
    [
        "Dhaka",
        "Washington DC", 
        "London", 
        "Berlin"
    ]
)
table.align = "l"


print(table)