import turtle as t
import winsound
import time
import random

#基本設定
t.bgcolor("lavender")
t.up()
t.speed(0)
t.goto(0, 220)
t.write("亀レース", False, "center", ("", 35))

#レース競技場書く
t.goto(-400, 170)
t.down()
t.color("lightPink")
t.begin_fill()
for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(400)
    t.right(90)
t.end_fill()

#決勝戦書く
t.color("black")
t.up()
t.goto(330, 200)
t.down()
t.goto(330, -250)

#亀選手生成
start_ycor = [150, 90, 30, -30, -90, -150, -210]
color_list = ["hotpink", "white", "red", "green", "yellow", "purple", "blue"]

#レースLINE生成
for i in range(6):
    t.up()
    t.goto(-400, start_ycor[i] - 30)
    t.color("white")
    t.down()
    t.goto(400, start_ycor[i] - 30)

turtles = []
for i in range(7):
    new_turtle = t.Turtle()
    new_turtle.up()
    new_turtle.shape("turtle")
    new_turtle.color(color_list[i])
    new_turtle.goto(-370, start_ycor[i])
    new_turtle.write(i+1)
    new_turtle.goto(-350, start_ycor[i]) #スタート線
    turtles.append(new_turtle)

#選択
user_choice = int(t.textinput("亀レース", "どんな亀が勝つでしょう?"))
t.up()
t.goto(0, -290)
t.color("black")
t.write(f"{user_choice}番亀を選択しました", False, "center", ("", 30))
t.ht()

#試合開始のお知らせ
winsound.Beep(523, 300)
time.sleep(0.3)

#試合開始
game_over = False
while not game_over:
    for i in turtles:
        rand_speed = random.randint(1, 10)
        i.forward(rand_speed)
        if i.xcor() > 330:
            game_over = True

# 1当を決める
max_xcor = 0
winner = 0
for i in range(len(turtles)):
    if turtles[i].xcor() > max_xcor:
        max.xcor = turtles[i].xcor()
        winner = i

#結果発表
t.goto(0, 0)
if user_choice == winner:
    t.write("成功！", False, "center", ("", 30))
else:
    t.write(f"失敗！{winner}番勝利", False, "center", ("", 30))

t.done()