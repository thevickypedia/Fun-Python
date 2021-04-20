from tkinter import Frame, Canvas, Label, TclError, N


class Pong(Frame):
    def __init__(self):
        """sets up windows and widgets"""
        Frame.__init__(self)
        self.master.title("Pong Game")
        self.grid()
        self.canvas_width = 800  # canvas width
        self.canvas_height = 400  # canvas height
        self.canvas = Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.grid()
        self.canvas.bind("<Left>", lambda event: self.move_paddle_left())
        self.canvas.bind("<Right>", lambda event: self.move_paddle_right())
        self.canvas.focus_set()
        diameter = 20  # ball diameter
        x = 2
        y = 2
        self.paddle_width = 80  # paddle length
        self.paddle_height = 20  # paddle height
        self._paddleTopX = 350
        self.lives = 5  # number of lives left
        self.scoreLabel = Label(self.master, font="Verdana 15", text="Lives Left: " + str(self.lives))
        self.scoreLabel.grid(row=0, column=0, sticky=N)
        # creates a label at the top of the frame
        self.isGameOver = Label(self.master, font="Verdana 15", text="Game Over")
        self.rect = self.canvas.create_rectangle(self.canvas_width / 2 - self.paddle_width / 2,
                                                 self.canvas_height - self.paddle_height,
                                                 self.canvas_width / 2 + self.paddle_width / 2, self.canvas_height,
                                                 fill="black", tags="paddle")
        self.ball = self.canvas.create_oval(x, y, x + diameter, y + diameter, fill="red", tags="ball")
        vertical = "south"
        horizontal = "right"
        dy = 2

        while True:
            """keeps track of ball and paddle movement"""
            if horizontal == "right":
                if x + diameter >= self.canvas_width:
                    horizontal = "left"
                else:
                    self.canvas.move("ball", dy, 0)
                    x += dy
            else:
                if x + diameter <= diameter:
                    horizontal = "right"
                else:
                    self.canvas.move("ball", -dy, 0)
                    x -= dy

            if y + diameter > self.canvas_height:
                self.lives -= 1
                self.scoreLabel.configure(text="Lives Left: " + str(self.lives))

            if self.lives <= 0:
                self.canvas.delete("ball", -x, -y)  # deletes the ball when game ends
                self.isGameOver.grid(row=0, column=0)  # Creates a label 'Game Over' when there are no lives left
                break

            if y + diameter >= self.canvas_height - self.paddle_height:
                if x + diameter > self._paddleTopX and x < self._paddleTopX + self.paddle_width:
                    vertical = "north"

            if vertical == "south":
                if y + diameter >= self.canvas_height:
                    vertical = "north"
                    self.canvas.move("ball", 0, -dy)
                    y += dy
                else:
                    self.canvas.move("ball", 0, dy)
                    y += dy
            else:
                if y + diameter <= diameter:
                    vertical = "south"
                else:
                    self.canvas.move("ball", 0, -dy)
                    y -= dy

            self.canvas.after(10)
            self.canvas.update()

    def move_paddle_left(self):
        """moves the paddle left with 5 pixels"""
        if self._paddleTopX >= 5:
            self._paddleTopX -= 5
            self.canvas.move("paddle", -5, 0)

    def move_paddle_right(self):
        """moves the paddle right with 5 pixels"""
        if self._paddleTopX + self.paddle_width < self.canvas_width:
            self._paddleTopX += 5
            self.canvas.move("paddle", 5, 0)


if __name__ == '__main__':
    try:
        Pong().mainloop()
    except (TclError, KeyboardInterrupt):
        pass
