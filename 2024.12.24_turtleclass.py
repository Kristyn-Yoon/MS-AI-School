from turtle import Turtle, Screen
import random

class CustomTurtle:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.screen = Screen()
        self.screen.onclick(self.draw_random_rectangle)

    def draw_random_rectangle(self, x, y):
        """
        Draws a rectangle with random size and colors at the clicked position.
        """
        size = random.randint(50, 200)  # Random size between 50 and 200
        pen_color = self.random_color()  # Random pen color
        fill_color = self.random_color()  # Random fill color

        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.color(pen_color, fill_color)
        self.turtle.begin_fill()

        for _ in range(4):
            self.turtle.forward(size)
            self.turtle.right(90)

        self.turtle.end_fill()

    def random_color(self):
        """
        Generates a random color in the format accepted by Turtle.
        """
        return (random.random(), random.random(), random.random())  # RGB tuple with random values

if __name__ == "__main__":
    # Set up the screen to handle color mode for RGB values
    screen = Screen()
    screen.colormode(1)  # RGB values between 0 and 1

    my_turtle = CustomTurtle()

    # Keeps the window open and ready for clicks
    screen.mainloop()
