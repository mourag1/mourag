import turtle

# إعداد الشاشة
wind = turtle.Screen()
wind.setup(800, 600)
wind.bgcolor("black")
wind.title("Hello in new")
wind.tracer(0)

# إعداد المضراب الأول
mdrab1 = turtle.Turtle()
mdrab1.speed(0)
mdrab1.color("blue")
mdrab1.shape("square")
mdrab1.shapesize(5, 1)
mdrab1.penup()
mdrab1.goto(350, 0)

# إعداد المضراب الثاني
mdrab2 = turtle.Turtle()
mdrab2.speed(0)
mdrab2.color("red")
mdrab2.shape("square")
mdrab2.shapesize(5, 1)
mdrab2.penup()
mdrab2.goto(-350, 0)

# إعداد الكرة
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# إعداد خط المنتصف
seek = turtle.Turtle()
seek.shape("square")
seek.shapesize(40, 0.01)
seek.penup()
seek.goto(0, 0)
seek.color("white")

# دوال حركة المضارب
def madrab1_up():
    y = mdrab1.ycor()
    if y < 250:  # الحد العلوي للمضرب
        y += 20
    mdrab1.sety(y)

def madrab1_down():
    y = mdrab1.ycor()
    if y > -250:  # الحد السفلي للمضرب
        y -= 20
    mdrab1.sety(y)

def madrab2_up():
    y = mdrab2.ycor()
    if y < 250:  # الحد العلوي للمضرب
        y += 20
    mdrab2.sety(y)

def madrab2_down():
    y = mdrab2.ycor()
    if y > -250:  # الحد السفلي للمضرب
        y -= 20
    mdrab2.sety(y)

    mdrab2.sety(y)

# الاستماع للوحة المفاتيح
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

    # إعداد كائن العداد
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# حلقة التحديث
while True:
    wind.update()
    
    # حركة الكرة
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # اصطدام الكرة بالجدران العلوية والسفلية
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  

    # إعادة الكرة إلى المنتصف إذا خرجت من الجدران اليمنى أو اليسرى
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
#faint start 
    # ارتطام الكرة بالمضرب الأول
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < mdrab1.ycor() + 50 and ball.ycor() > mdrab1.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    # ارتطام الكرة بالمضرب الثاني
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < mdrab2.ycor() + 50 and ball.ycor() > mdrab2.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        

# إضافة متغيرات لتسجيل النقاط
    score_a = 0
    score_b = 0

    # إعداد كائن العداد
    # تحديث العداد
    def update_score():
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # تعديل النقاط عند خروج الكرة من الشاشة
    if ball.xcor() > 390:
        score_a += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1
