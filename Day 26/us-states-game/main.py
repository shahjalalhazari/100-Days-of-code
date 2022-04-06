import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read CSV file 50 States
data = pandas.read_csv("50_states.csv")
# Make a list of all the states
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    state_name = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct.",
        prompt="What's another state name?"
    ).title()

    if state_name == "Exit":
        ##  Condition with List Comprehension.
        missing_states = [state for state in all_states if state not in guessed_states]
        #  This above line of code is replace 3 lines of code.

        ## Old code for above condition.
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing_states_list.csv")
        break

    if state_name in all_states:
        guessed_states.append(state_name)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Get State data based on user input.
        state_data = data[data.state == state_name]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_name.title())

screen.exitonclick()
