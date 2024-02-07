import tkinter as tk
import random
from tkinter.colorchooser import askcolor
from math import pi, cos, sin, sqrt
from flask import Flask, render_template

app = Flask(__name__)

class ShapeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Generator")

        canvas_frame = tk.Frame(root)
        canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(canvas_frame, width=500, height=500, bg="#0066CC")  # Set background color to 0066CC
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame for the information below the canvas
        info_frame = tk.Frame(root)
        info_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Add a vertical scrollbar to the info_frame
        info_scrollbar = tk.Scrollbar(info_frame, orient=tk.VERTICAL)
        info_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.shapes_count_label = tk.Label(info_frame, text="0", font=("Helvetica", 60))
        self.shapes_count_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Configure the scrollbar to scroll the info_frame
        info_scrollbar.configure(command=self.shapes_count_label.yview)
        self.shapes_count_label.configure(yscrollcommand=info_scrollbar.set)

        self.canvas = tk.Canvas(self.root, width=500, height=500, bg="#0066CC")  # Set background color to 0066CC
        self.canvas.pack()

        self.shapes_count_label = tk.Label(root, text="0", font=("Helvetica", 60))
        self.shapes_count_label.pack()

        shape_label_1 = tk.Label(root, text="Shape / Color 1:")
        shape_label_1.pack()

        self.shape_var_1 = tk.StringVar(value="Square")  # Set default shape to Square
        shapes = ["Circle", "Square", "Triangle", "Diamond", "Hexagon", "Trapezoid"]
        shape_dropdown_1 = tk.OptionMenu(root, self.shape_var_1, *shapes)
        shape_dropdown_1.pack()

        self.color_var_1 = tk.StringVar(value="Blue")  # Set default color to Blue
        colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Cyan"]
        color_dropdown_1 = tk.OptionMenu(root, self.color_var_1, *colors)
        color_dropdown_1.pack()

        shape_label_2 = tk.Label(root, text="Shape / Color 2:")
        shape_label_2.pack()

        self.shape_var_2 = tk.StringVar(value="Circle")  # Set default shape to Circle
        shape_dropdown_2 = tk.OptionMenu(root, self.shape_var_2, *shapes)
        shape_dropdown_2.pack()

        self.color_var_2 = tk.StringVar(value="Yellow")  # Set default color to Yellow
        color_dropdown_2 = tk.OptionMenu(root, self.color_var_2, *colors)
        color_dropdown_2.pack()

        def toggle_lock_number(self):
            if self.lock_num_var.get():
                self.num_shapes_var.set(self.num_shapes_var.get())

        def check_overlap(self, x, y, size, positions):
            for pos_x, pos_y, pos_size in positions:
                distance = sqrt((x - pos_x)**2 + (y - pos_y)**2)
                min_distance = size + pos_size + 10  # 10 is a buffer to ensure shapes don't touch
                if distance < min_distance:
                    return True
            return False

        def navigate_backward(self):
            pass

        def generate_triangle_points(self, x, y, size):
            return [x, y - size, x + size, y + size, x - size, y + size]

        def generate_square_points(self, x, y, size, angle):
            angle_rad = pi / 180 * angle
            points = [x + size * cos(angle_rad), y + size * sin(angle_rad),
                      x - size * sin(angle_rad), y + size * cos(angle_rad),
                      x - size * cos(angle_rad), y - size * sin(angle_rad),
                      x + size * sin(angle_rad), y - size * cos(angle_rad)]
            return points

        def generate_rectangle_points(self, x, y, size, angle):
            angle_rad = pi / 180 * angle
            points = [x + size * 1.5 * cos(angle_rad), y + size * 1.5 * sin(angle_rad),
                      x - size * 0.5 * sin(angle_rad), y + size * 0.5 * cos(angle_rad),
                      x - size * 1.5 * cos(angle_rad), y - size * 1.5 * sin(angle_rad),
                      x + size * 0.5 * sin(angle_rad), y - size * 0.5 * cos(angle_rad)]
            return points

        def generate_hexagon_points(self, x, y, size, angle):
            points = []
            for i in range(6):
                angle_rad = pi / 180 * (60 * i + angle)
                points.extend([x + size * cos(angle_rad), y + size * sin(angle_rad)])
            return points

        def generate_trapezoid_points(self, x, y, size, angle):
            angle_rad = pi / 180 * angle
            points = [x + size * cos(angle_rad), y + size * sin(angle_rad),
                      x - size * 2 * sin(angle_rad), y + size * 2 * cos(angle_rad),
                      x - size * 3 * cos(angle_rad), y - size * 3 * sin(angle_rad),
                      x + size * 2 * sin(angle_rad), y - size * 2 * cos(angle_rad)]
            return points

        @app.route("/")
        def index():
            root = tk.Tk()
            app = ShapeGenerator(root)
            root.mainloop()
            return render_template("index.html")

        if __name__ == "__main__":
            app.run()
