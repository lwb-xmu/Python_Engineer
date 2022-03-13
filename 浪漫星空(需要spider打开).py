import turtle
import random 
turtle.speed(0) # 最快速度
turtle.bgcolor('black') # 改变背景色
turtle.color('white') # 改变画笔颜色
turtle.pensize(2) # 改变画笔粗细
acc_ext = 0 # 累计圆弧
r = 10
turtle.penup() # 抬起画笔
turtle.goto(0, -r) # 指定画笔位置
turtle.pendown() # 放下画笔

while True:
    turtle.color(random.choice(['white', 'black']) # 随机黑白画笔
	ext = random.random() * 90 # 随机弧度
	turtle.circle(r, ext) # 画圆弧
	acc_ext += ext
	if acc_ext > 360:
	    acc_ext = 0
		turtle.penup() # 抬起画笔
		turtle.goto(-r) # 移动到合适位置
		turtle.setheading(0) # 摆正画笔朝向
		turtle.pendown() # 落笔
		r += 3