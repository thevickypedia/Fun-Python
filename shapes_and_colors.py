"""Rectangle and Oval shapes with colors filled."""

from tkinter import Frame, Canvas, Radiobutton, Checkbutton, Button, W, E, N


class Geometry(Frame):
    def __init__(self):
        """Sets up windows and widgets"""
        Frame.__init__(self)
        self.master.title("Canvas")
        self.grid()
        self.canvas = Canvas(self, width=300, height=300, bg='white')
        self.canvas.grid()
        self.r1 = Radiobutton(self, text="Rectangle", command=self.create_rectangle)
        self.r1.grid(row=1, column=0, sticky=W)
        self.r1.deselect()
        self.r2 = Radiobutton(self, text="Oval", command=self.create_oval)
        self.r2.grid(row=1, column=0, sticky=N)
        self.r2.deselect()
        self.r3 = Checkbutton(self, text="Filled", command=self.is_filled)
        self.r3.grid(row=1, column=0, sticky=E)
        self.b1 = Button(self, text="Clear", command=self.clear_frame)
        self.b1.grid(row=2, column=0)
        self.oval_created = False
        self.rect_created = False

    def create_rectangle(self, color=None):
        """Creates a rectangle"""
        self.rect_created = True
        self.canvas.create_rectangle(50, 50, 250, 250, fill=color)

    def rectangle_is_filled(self):
        """Calls createRectangle passing the color argument"""
        self.create_rectangle(color='red')

    def clear_frame(self):
        """Deletes the entire canvas"""
        self.oval_created = False
        self.rect_created = False
        self.canvas.delete("all")
        self.r1.deselect()
        self.r2.deselect()
        self.r3.deselect()

    def create_oval(self, color=None):
        """Create an oval"""
        self.oval_created = True
        self.canvas.create_oval(50, 100, 250, 200, fill=color)

    def oval_is_filled(self):
        """Calls createOval passing the color argument"""
        self.create_oval(color='yellow')

    def is_filled(self):
        """Checks if rectangle is created and then calls rectangleIsFilled, and
        checks if oval is created and then calls ovalIsFilled"""
        if self.rect_created:
            self.rectangle_is_filled()
        if self.oval_created:
            self.oval_is_filled()


if __name__ == '__main__':
    Geometry().mainloop()
