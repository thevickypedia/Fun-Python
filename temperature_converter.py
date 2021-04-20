"""Widget to convert temperature between Fahrenheit, Celsius and Kelvin."""

from tkinter import Frame, Label, DoubleVar, Button, Entry


class TemperatureConversion(Frame):
    def __init__(self):
        """Sets up windows and widgets"""
        Frame.__init__(self)
        self.master.title("Temperature Converter")
        self.grid()
        self.label1 = Label(self, text="Fahrenheit")
        self.label1.grid(row=0, column=0)
        self.label1var = DoubleVar(self, 32.0)
        self.label1entry = Entry(self, textvariable=self.label1var)
        self.label1entry.grid(row=1, column=0)
        self.label1button = Button(self, text="Convert From Fahrenheit", command=self.to_celsius)
        self.label1button.grid(row=2, column=0)

        self.label2 = Label(self, text="Celsius")
        self.label2.grid(row=0, column=1)
        self.label2var = DoubleVar()
        self.label2entry = Entry(self, textvariable=self.label2var)
        self.label2entry.grid(row=1, column=1)
        self.label2button = Button(self, text="Convert From Celsius", command=self.to_fahrenheit)
        self.label2button.grid(row=2, column=1)

        self.label3 = Label(self, text="Kelvin")
        self.label3.grid(row=0, column=2)
        self.label3var = DoubleVar(self, 273.15)
        self.label3entry = Entry(self, textvariable=self.label3var)
        self.label3entry.grid(row=1, column=2)
        self.label3button = Button(self, text="Convert From Kelvin", command=self.to_kelvin)
        self.label3button.grid(row=2, column=2)

    def to_celsius(self):
        """converts fahrenheit to celsius"""
        fahrenheit = self.label1var.get()
        celsius = (fahrenheit - 32) * 5/9
        self.label2var.set(f"{round(float(celsius), 2)}")

    def to_fahrenheit(self):
        """converts celsius to fahrenheit"""
        celsius = self.label2var.get()
        fahrenheit = (celsius * 9/5) + 32
        self.label1var.set(f"{round(float(fahrenheit), 2)}")

    def to_kelvin(self):
        """converts fahrenheit and celsius to kelvin"""
        kelvin = None
        fahrenheit = self.label1var.get()
        celsius = self.label2var.get()
        if fahrenheit:
            kelvin = (fahrenheit - 32) * 5/9 + 273.15
        if celsius:
            kelvin = celsius + 273.15
        self.label3var.set(f"{round(float(kelvin), 2)}")


if __name__ == '__main__':
    TemperatureConversion().mainloop()
