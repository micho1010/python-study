# class Ball:

#     def bounce(self):
#         if self.direction == "up":
#             self. direction = "down"
#         else:
#             self.direction = "up"

# myBall = Ball()
# myBall.direction = "down"
# myBall.color = "red"
# myBall.size = "small"

# print("I just created a ball.")
# print("My ball is", myBall.size)
# print("My ball is", myBall.color)
# print("My ball's direction is", myBall.direction)
# print("Now I'm going to bounce the ball")
# print()
# myBall.bounce()
# print("Now the ball's direction is", myBall.direction)


class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        msg = "Hi, I'm a " + self.size + " " + self.color + " ball!"
        return msg


myBall = Ball("red", "small", "down")
print(myBall)
