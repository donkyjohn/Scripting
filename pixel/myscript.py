import tkinter as tk
import random
from tkinter.colorchooser import askcolor
from math import pi, cos, sin, sqrt

class ShapeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Generator")

        self.canvas = tk.Canvas(self.root, width=250, height=250, bg="#0066CC")  # Set background color to 0066CC
        self.canvas.pack(side=tk.TOP)

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

        self.num_shapes_var = tk.IntVar(value=10)  # Set default number of objects to 10
        num_shapes_slider_label = tk.Label(root, text="Number of Shapes:")
        num_shapes_slider_label.pack()
        num_shapes_slider = tk.Scale(root, from_=1, to=25, orient=tk.HORIZONTAL, variable=self.num_shapes_var)  # Set max to 25
        num_shapes_slider.pack()

        self.lock_num_var = tk.BooleanVar(value=False)
        lock_num_checkbox = tk.Checkbutton(root, text="Lock Number", variable=self.lock_num_var, command=self.toggle_lock_number)
        lock_num_checkbox.pack()

        self.allow_overlap_var = tk.BooleanVar(value=False)
        allow_overlap_button = tk.Checkbutton(root, text="Allow Overlap", variable=self.allow_overlap_var)
        allow_overlap_button.pack()

        self.auto_gen_var = tk.BooleanVar(value=True)
        auto_gen_checkbox = tk.Checkbutton(root, text="Auto-Generate", variable=self.auto_gen_var, command=self.toggle_auto_generation)
        auto_gen_checkbox.pack()

        delay_label = tk.Label(root, text="Delay (seconds):")
        delay_label.pack()

        self.delay_var = tk.DoubleVar(value=2.5)  # Set default delay to 2.5 seconds
        delay_slider = tk.Scale(root, from_=1, to=10, resolution=0.1, orient=tk.HORIZONTAL, variable=self.delay_var)
        delay_slider.pack()

        next_button = tk.Button(root, text="Next", command=self.generate_shapes)
        next_button.pack()

        self.start_stop_button = tk.Button(root, text="Start", command=self.toggle_auto_generation)
        self.start_stop_button.pack()

        background_color_button = tk.Button(root, text="Change Background Color", command=self.change_background_color)
        background_color_button.pack()

        self.next_shape_event = None
        self.shapes_count = 0  # Variable to store the previous count

        self.root.bind("<space>", lambda event: self.generate_shapes())
        self.root.bind("<Return>", lambda event: self.toggle_auto_generation())
        self.root.bind("<Right>", lambda event: self.navigate_forward())

        self.generate_shapes()  # Initial generation

    def toggle_auto_generation(self):
        self.auto_gen_var.set(not self.auto_gen_var.get())
        if self.auto_gen_var.get():
            self.auto_gen_var.set(0)
            self.start_stop_button.config(text="Start")
        
        else:
            self.auto_gen_var.set(1)
            self.start_stop_button.config(text="Stop")
            self.schedule_next_shape()

    def schedule_next_shape(self):
        delay = int(self.delay_var.get() * 1000)
        if self.next_shape_event:
            self.root.after_cancel(self.next_shape_event)
        if self.auto_gen_var.get():
            self.next_shape_event = self.root.after(delay, self.generate_shapes)

    def generate_shapes(self):
        self.canvas.delete("all")

        shape_var_1 = self.shape_var_1.get()
        color_var_1 = self.color_var_1.get()
        shape_var_2 = self.shape_var_2.get()
        color_var_2 = self.color_var_2.get()

        num_shapes = self.num_shapes_var.get() if self.lock_num_var.get() else random.randint(1, self.num_shapes_var.get())

        positions = []  # List to store positions of generated shapes

        for _ in range(num_shapes):
            x = random.randint(50, 450)
            y = random.randint(50, 450)
            size = random.randint(20, 50)
            rotation_angle = random.uniform(0, 360)

            if random.choice([1, 2]) == 1:
                selected_shape = shape_var_1
                selected_color = color_var_1
            else:
                selected_shape = shape_var_2
                selected_color = color_var_2

            overlapping = self.check_overlap(x, y, size, positions) if not self.allow_overlap_var.get() else False

            while overlapping:
                x = random.randint(50, 450)
                y = random.randint(50, 450)
                size = random.randint(20, 50)
                overlapping = self.check_overlap(x, y, size, positions) if not self.allow_overlap_var.get() else False

            positions.append((x, y, size))

            if selected_shape == "Circle":
                shape_id = self.canvas.create_oval(x, y, x + size, y + size, fill=selected_color, outline="white")
            elif selected_shape == "Square":
                points = self.generate_square_points(x, y, size, rotation_angle)
                shape_id = self.canvas.create_polygon(*points, fill=selected_color, outline="white")
            elif selected_shape == "Triangle":
                points = self.generate_triangle_points(x, y, size)
                shape_id = self.canvas.create_polygon(*points, fill=selected_color, outline="white")
            elif selected_shape == "Diamond":
                points = self.generate_rectangle_points(x, y, size, rotation_angle)
                shape_id = self.canvas.create_polygon(*points, fill=selected_color, outline="white")
            elif selected_shape == "Hexagon":
                angle = random.uniform(0, 360)
                points = self.generate_hexagon_points(x, y, size, angle)
                shape_id = self.canvas.create_polygon(*points, fill=selected_color, outline="white")
            elif selected_shape == "Trapezoid":
                size *= 0.5  # Reduce size by 50%
                points = self.generate_trapezoid_points(x, y, size, rotation_angle)
                shape_id = self.canvas.create_polygon(*points, fill=selected_color, outline="white")

        if self.auto_gen_var.get():
            self.schedule_next_shape()

        self.update_shapes_count()

    def check_overlap(self, x, y, size, positions):
        for pos_x, pos_y, pos_size in positions:
            distance = sqrt((x - pos_x)**2 + (y - pos_y)**2)
            min_distance = size + pos_size + 10  # 10 is a buffer to ensure shapes don't touch
            if distance < min_distance:
                return True
        return False

    def update_shapes_count(self):
        self.shapes_count_label.config(text=f"{self.shapes_count}")
        self.shapes_count = len(self.canvas.find_all())

    def navigate_forward(self):
        self.shapes_count_label.config(text=f"{self.shapes_count}")  # Update the count to the previous one
        self.generate_shapes()

    def navigate_backward(self):
        # Add logic to navigate backward
        pass

    def change_background_color(self):
        _, color = askcolor()
        if color:
            self.canvas.configure(bg=color)

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

    def toggle_lock_number(self):
        if self.lock_num_var.get():
            self.num_shapes_var.set(self.num_shapes_var.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeGenerator(root)
    root.mainloop()

