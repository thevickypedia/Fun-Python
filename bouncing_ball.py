"""Bouncing ball that changes color and speed on each bounce."""

from random import choice
from tkinter import Frame, Canvas, TclError


class Pong(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Bouncing Ball")
        self.grid()
        canvas_width = 800  # canvas width
        canvas_height = 400  # canvas height
        self.canvas = Canvas(self, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.grid()
        diameter = 20  # ball diameter
        x = 2
        y = 2
        speed = 20
        self.canvas.create_oval(x, y, x + diameter, y + diameter, fill="red", tags="ball")
        color = ['red', 'green', 'blue', 'orange', 'yellow', 'pink', 'turquoise', 'grey', 'black', 'brown', 'maroon']
        direction = "down"  # ball direction
        dy = 2
        # move ball
        reverse = False
        color_check = None
        while True:
            """keep track of ball's movement, update direction,and draw ball as needed"""
            if direction == "down":
                if reverse:
                    self.canvas.move("ball", -2, dy)  # direction is changed to negative to start reverse motion
                else:
                    self.canvas.move("ball", 2, dy)
                y += dy
                if y + diameter >= canvas_height:
                    direction = "up"
            else:
                if reverse:
                    self.canvas.move("ball", -2, -dy)  # direction is changed to negative to start reverse motion
                else:
                    self.canvas.move("ball", 2, -dy)
                y -= dy
                if y <= 0 and reverse:
                    direction = "up"
                elif y <= 0:
                    direction = "down"
                    reverse = True  # reverse is set to True so that the ball changes to reverse direction
                if y < 0:
                    reverse = False  # resets reverse to start from old spot after completing journey on whole window
            if direction != color_check and y != 2:  # color check is set so that colors are changed while hit a corner
                self.canvas.itemconfig("ball", fill=choice(color))  # keeps picking random colors
                color_check = direction  # sets direction to color_check so that change is picked by the above condition
                if speed >= 0:
                    speed -= 3  # speed keeps changing everytime the ball color changes
                else:
                    speed = 40  # speed resets to initial value when decremented to 0 or less
            self.canvas.after(speed)  # speed is set outside the condition so ball movement is not affected by change
            self.canvas.update()


if __name__ == '__main__':
    try:
        Pong().mainloop()
    except (TclError, KeyboardInterrupt):
        pass
