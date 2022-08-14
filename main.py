import turtle,pandas

name = turtle.Turtle()
screen = turtle.Screen()
promoter = turtle.Turtle()

screen.title('U.S. States Game')

map_image = "C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\OOP\\us-states-game-start\\blank_states_img.gif"

turtle.addshape(map_image)
turtle.shape(map_image)


axes = pandas.read_csv("C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\OOP\\us-states-game-start\\50_states.csv")
states = axes.state
s = states.to_list()
guessed_states = []
states_to_learn = []
score = 0
game = True
while score < 50:
    promoter.hideturtle()
    promoter.clear()
    guess = turtle.textinput(f"{score}/50 Correct", prompt='Name a State').title()
    if guess == "Exit":
        for i in s:
            if i not in guessed_states:
                states_to_learn.append(i)
        states_to_learn.to_csv("C:\\Users\\Elorm\\Desktop\\Code\\100Days of Coding Challenge\\OOP\\us-states-game-start\\states_to_learn.csv")           
        break
    if guess in s and guess not in guessed_states:
        a = int(axes.x[axes.state == guess])
        b = int(axes.y[axes.state == guess])
        guessed_states.append(guess)
        score += 1
        name.hideturtle()
        name.write(guess, align="center", font=('Calibri',11,'normal'))
        name.penup()
        name.goto(a,b)
    elif guess in s and guess in guessed_states:
        promoter.hideturtle()
        promoter.penup()
        promoter.goto(0,300)
        promoter.write("Try again, State Already Named", align="center", font=('Calibri',12,'normal'))
    elif guess not in s:
        promoter.hideturtle()
        promoter.penup()
        promoter.goto(0,300)
        promoter.write("Try again, State Not Found", align="center", font=('Calibri',12,'normal'))



print(states_to_learn)

