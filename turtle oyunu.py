import turtle
import random

game_screen = turtle.Screen()
FONT = ("Arial", 30, "normal")
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
score = 0
turtle_list= [] 
game_over = False


def screen_score():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_height = game_screen.window_height() / 2 
    y = top_height * 0.8 
    score_turtle.setpos(0, y)
    
    score_turtle.write(arg="Score: 0", move=False, align="center", font=(FONT))


print(screen_score())
grid_size = 10



def make_turtle(x,y):
    t = turtle.Turtle()
   
    def hand_click(x, y): 
        global score 
        score += 1      
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=(FONT))


    t.onclick(hand_click)   
    t.penup()
    t.shape("turtle")
    t.shapesize(1.5,1.5)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t) 


x_cordi = [-20, -10, 0, 10, 20]
y_cordi = [20, 10, 0, -10, ]
def setup_turtle():
    for x in x_cordi:
        for y in y_cordi:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        game_screen.ontimer(show_turtles, 500) 

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()
    top_height = game_screen.window_height() / 2 
    y = top_height * 0.8 
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Timer: {}".format(time), move=False, align="center", font=(FONT))
        game_screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="game over", move=False, align="center", font=(FONT))

turtle.tracer(0)       
print(setup_turtle())
hide_turtles()
print(show_turtles())
print(countdown(10))
turtle.tracer(1)        

turtle.mainloop()
