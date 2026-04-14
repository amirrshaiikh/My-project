# import colorgram
# rgb_colors=[]
# lits=colorgram.extract("image.jpg", 20)
# # print(lits)
# for color in lits:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)
import turtle as t



colorlist=[ (237, 36, 110), (147, 25, 69), (214, 168, 52), (240, 73, 36), (9, 146, 93), (187, 160, 41), (26, 126, 193),
            (46, 190, 233), (252, 223, 0), (241, 219, 64), (124, 192, 82), (82, 21, 82), (187, 37, 102), (27, 171, 123),
            (218, 58, 24), (209, 131, 168)]
tim=t.Turtle()
tim.hideturtle()
screen=t.Screen()
screen.colormode(255)
screen.setup(width=700, height=640)
tim.width(30)
tim.speed(0)
tim.teleport(-310, -270)
def dodod(colorlist):
    to=0
    for j in range(10):
        x=tim.xcor()
        y=tim.ycor()
        for i in range(10):
            to+=1
            num=to%len(colorlist)
            tim.color(colorlist[num])
            tim.dot(40, colorlist[num])
            tim.penup()
            tim.forward(65)
            tim.pendown()
        tim.teleport(x, y+60)


dodod(colorlist)
screen.exitonclick()