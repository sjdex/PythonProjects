import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
df = pd.read_csv("50_states.csv")
us_states_list = df["state"].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Whats another State's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in us_states_list:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        pd.DataFrame(missing_states).to_csv("States_to_Learn.csv")
        break

    if answer_state in us_states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
