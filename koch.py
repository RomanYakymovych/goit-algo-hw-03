import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


if __name__ == "__main__":
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()

    my_turtle.speed(0)  # Fastest speed
    my_turtle.color("blue")

    # Move the turtle into position
    my_turtle.penup()
    my_turtle.goto(-150, 90)
    my_turtle.pendown()

    # Draw the snowflake
    for _ in range(3):
        koch_snowflake(my_turtle, 4, 300)
        my_turtle.right(120)

    my_win.mainloop()
