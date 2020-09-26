# test if this shows up on GIT again

import turtle as trt

wn = trt.Screen()
wn.title("Pong by Leon")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

#  Paddle A
paddle_a = trt.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-380, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)


#  Paddle B
paddle_b = trt.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(380, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#  Ball
ball = trt.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Score keeper
pen = trt.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player A: 0        Player B: 0", align="center", font=("courier", 16, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_dn():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_dn():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_dn, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_dn, "Down")


# Main game loop
while True:
    wn.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # upper and lower border bounce
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.dy *= -1

    # Ball goes past paddle
    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}        Player B: {}".format(score_a, score_b), align="center", font=("courier", 16, "normal"))

    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}        Player B: {}".format(score_a, score_b), align="center", font=("courier", 16, "normal"))

    # Paddle collision detection
    # Paddle A
    if (ball.xcor() < -370 and ball.xcor() > -390) and (ball.ycor() < (paddle_a.ycor() + 50) and (ball.ycor() > (paddle_a.ycor() - 50))):
        ball.dx *= -1
    # Paddle b
    if (ball.xcor() > 370 and ball.xcor() < 390) and (ball.ycor() < (paddle_b.ycor() + 50) and (ball.ycor() > (paddle_b.ycor() - 50))):
        ball.dx *= -1


