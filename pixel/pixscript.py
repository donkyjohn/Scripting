import tkinter as tk
import random

class SG:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Generator")

        self.canvas = tk.Canvas(self.root, height=500, width=500, bg="#0066CC")
        self.canvas.pack()

        self.counter = tk.Label(root, text="0", font=("Helvetica", 60))
        self.counter.pack()

        self.create_option_widgets("Shape / Color 1:", "Circle", "Blue")
        self.create_option_widgets("Shape / Color 2:", "Circle", "Blue")

    def create_option_widgets(self, label_text, default_shape, default_color):
        label = tk.Label(self.root, text=label_text)
        label.pack()

        shape_var = tk.StringVar(value=default_shape)
        shapes = ["Circle", "Square", "Triangle", "Diamond", "Hexagon", "Trapezoid"]
        shape_dropdown = tk.OptionMenu(self.root, shape_var, *shapes)
        shape_dropdown.config(width=11, bg="white", fg="black", relief=tk.SUNKEN, borderwidth=2)
        shape_dropdown.pack()

        color_var = tk.StringVar(value=default_color)
        colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Cyan"]
        color_dropdown = tk.OptionMenu(self.root, color_var, *colors)
        color_dropdown.config(width=11, bg="white", fg="black", relief=tk.SUNKEN, borderwidth=2)
        color_dropdown.pack()


root = tk.Tk()
app = SG(root)
root.mainloop()
