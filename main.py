import turtle
import pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states = states_data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for i in states:
            if i not in guessed_states:
                missing_states.append(i)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if answer_state in states:
        state_turtle = Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_data = states_data[states_data["state"] == answer_state]
        state_turtle.goto(state_data.x.item(), state_data.y.item())
        state_turtle.write(state_data.state.item())
        guessed_states.append(answer_state)












