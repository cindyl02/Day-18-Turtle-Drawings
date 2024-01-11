import turtle as t
import random

# import colorgram


COLOURS = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
DIRECTIONS = [0, 90, 100, 270]


##### Random Walk #####
def random_walk():
    for _ in range(200):
        tim.pencolor(random.choice(COLOURS))
        tim.forward(30)
        tim.setheading(random.choice(DIRECTIONS))


##### Spirograph #####
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random.choice(COLOURS))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

##### Hirst Painting #####
def hirst_painting():
    # colors = colorgram.extract('image.jpg', 30)
    # print([(c.rgb.r, c.rgb.g, c.rgb.b) for c in colors])
    color_list = [(236, 35, 108), (221, 232, 237), (146, 28, 66), (239, 75, 35), (230, 237, 232), (7, 148, 94),
                  (220, 171, 45), (182, 159, 48), (44, 191, 232), (28, 126, 194), (253, 223, 0), (125, 192, 79),
                  (84, 28, 91), (245, 219, 50), (179, 40, 98), (42, 169, 116), (209, 131, 165), (205, 56, 35),
                  (239, 161, 192), (148, 25, 24), (242, 168, 156), (162, 211, 178), (26, 187, 225), (138, 210, 232),
                  (7, 114, 55), (76, 135, 183), (112, 10, 8), (176, 190, 221)]
    t.colormode(255)
    tim = t.Turtle()
    tim.speed("fastest")
    tim.hideturtle()
    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    for count in range(1, 101):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        if count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

tim = t.Turtle()
tim.speed("fastest")
tim.pensize(15)
draw_spirograph(5)
# random_walk()
# hirst_painting()