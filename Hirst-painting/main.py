from turtle import Turtle, Screen
import random

# import colorgram

# colors = colorgram.extract('image.jpg', 84)
# rgb_tuples = []
# for color in colors:
#     for _ in range(0,len(colors) - 1):
#         rgb_tuples.append(tuple(colors[_].rgb))
#
# print(rgb_tuples)
color_list = [(202, 165, 110), (152, 76, 51), (54, 94, 123), (222, 201, 138), (167, 152, 45), (134, 33, 22),
              (133, 163, 184), (195, 93, 74), (49, 122, 87), (74, 42, 35), (16, 96, 73), (146, 178, 149),
              (92, 73, 75), (231, 176, 166), (160, 143, 158), (53, 47, 50), (184, 204, 172), (36, 61, 76),
              (23, 84, 88), (145, 21, 23), (86, 145, 129), (42, 66, 87), (14, 70, 64), (106, 128, 153),
              (169, 101, 102), (70, 64, 56), (176, 192, 210), (112, 135, 137), (209, 183, 187), (246, 243, 238),
              (246, 242, 244), (202, 165, 110), (240, 246, 242), (237, 240, 244), (152, 76, 51), (54, 94, 123),
              (134, 33, 22), (133, 163, 184), (195, 93, 74), (49, 122, 87), (74, 42, 35), (16, 96, 73), (146, 178, 149),
              (92, 73, 75), (231, 176, 166), (160, 143, 158), (53, 47, 50), (184, 204, 172), (36, 61, 76), (23, 84, 88),
              (145, 21, 23), (86, 145, 129), (42, 66, 87), (14, 70, 64), (106, 128, 153), (169, 101, 102), (70, 64, 56),
              (176, 192, 210), (112, 135, 137), (209, 183, 187), (246, 243, 238), (246, 242, 244), (202, 165, 110),
              (240, 246, 242), (237, 240, 244), (152, 76, 51), (54, 94, 123), (222, 201, 138), (167, 152, 45),
              (240, 246, 242), (237, 240, 244), (152, 76, 51), (54, 94, 123), (222, 201, 138), (167, 152, 45),
              (134, 33, 22), (133, 163, 184), (195, 93, 74), (49, 122, 87), (74, 42, 35), (16, 96, 73), (146, 178, 149),
              (92, 73, 75), (231, 176, 166), (160, 143, 158), (53, 47, 50), (184, 204, 172), (36, 61, 76), (23, 84, 88),
              (145, 21, 23), (86, 145, 129), (42, 66, 87), (14, 70, 64), (106, 128, 153), (169, 101, 102), (70, 64, 56),
              (176, 192, 210), (112, 135, 137), (209, 183, 187), (246, 243, 238), (246, 242, 244), (202, 165, 110),
              (240, 246, 242), (237, 240, 244), (152, 76, 51), (54, 94, 123), (222, 201, 138), (167, 152, 45),
              (134, 33, 22), (133, 163, 184), (195, 93, 74), (49, 122, 87), (74, 42, 35), (16, 96, 73), (146, 178, 149),
              (92, 73, 75), (231, 176, 166), (160, 143, 158), (53, 47, 50), (184, 204, 172), (36, 61, 76), (23, 84, 88),
              (145, 21, 23), (86, 145, 129), (42, 66, 87), (14, 70, 64), (106, 128, 153), (169, 101, 102), (70, 64, 56),
              (176, 192, 210), (112, 135, 137), (209, 183, 187), (246, 243, 238), (246, 242, 244), (202, 165, 110),
              (240, 246, 242), (237, 240, 244), (152, 76, 51), (54, 94, 123), (222, 201, 138), (167, 152, 45),
              (134, 33, 22), (133, 163, 184), (195, 93, 74), (49, 122, 87), (74, 42, 35), (16, 96, 73), (146, 178, 149),
              (92, 73, 75), (231, 176, 166), (160, 143, 158), (53, 47, 50), (184, 204, 172), (36, 61, 76), (23, 84, 88),
              (145, 21, 23), (86, 145, 129), (42, 66, 87), (14, 70, 64), (106, 128, 153), (169, 101, 102), (70, 64, 56),
              (176, 192, 210), (112, 135, 137), (209, 183, 187), (246, 243, 238), (246, 242, 244), (202, 165, 110),
              (240, 246, 242), (237, 240, 244), (152, 76, 51), (54, 94, 123), (222, 201, 138), (167, 152, 45),
              (134, 33, 22), (133, 163, 184), (195, 93, 74), (49, 122, 87), (74, 42, 35), (16, 96, 73), (146, 178, 149),
              (92, 73, 75), (231, 176, 166), (160, 143, 158), (53, 47, 50), (184, 204, 172), (36, 61, 76), (23, 84, 88),
              ]

dot = Turtle()
dot.speed('fastest')
dot.pensize(20)
screen = Screen()
screen.colormode(255)

def draw_row(circle, nr_circles_in_row):
    """It draws an entire row of circles of diameter 20 and distance of 50 from each other."""
    for _ in range(nr_circles_in_row):
        circle.color(random.choice(color_list))
        circle.dot(20, )
        circle.penup()
        circle.forward(50)
        circle.pendown()


def invert_position(circle):
    """It inverts the position of the cursor and moves one row up after the row is finished."""
    if circle.heading() == 0:
        for _ in range(2):
            circle.penup()
            circle.left(90)
            circle.forward(50)
    elif circle.heading() == 180:
        for _ in range(2):
            circle.penup()
            circle.right(90)
            circle.forward(50)

for _ in range(10):
    draw_row(dot, 10)
    invert_position(dot)

screen.exitonclick()
