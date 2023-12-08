from tkinter import simpledialog, Tk, Canvas, Frame, Button, Menu, PhotoImage, filedialog

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.canvas_width = 800
        self.canvas_height = 600

        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bd=0, highlightthickness=0)
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.draw)
        self.color = "black"  # Default color
        self.brush_size = 2  # Default brush size
        self.brush_shape = "circle"  # Default brush shape
        self.eraser_mode = False  # Eraser mode flag

        self.create_brush_size_buttons()
        self.create_brush_shape_buttons()
        self.create_eraser_button()

    def draw(self, event):
        x, y = event.x, event.y
        if self.eraser_mode:
            self.canvas.create_rectangle(x - self.brush_size, y - self.brush_size, x + self.brush_size,
                                         y + self.brush_size, fill="white", outline="")
        else:
            if self.brush_shape == "circle":
                self.canvas.create_oval(x - self.brush_size, y - self.brush_size, x + self.brush_size,
                                        y + self.brush_size, fill=self.color, outline="")
            elif self.brush_shape == "square":
                self.canvas.create_rectangle(x - self.brush_size, y - self.brush_size, x + self.brush_size,
                                             y + self.brush_size, fill=self.color, outline="")
            elif self.brush_shape == "triangle":
                self.canvas.create_polygon(x, y - self.brush_size, x - self.brush_size, y + self.brush_size,
                                           x + self.brush_size, y + self.brush_size, fill=self.color, outline="")
            elif self.brush_shape == "line":
                self.canvas.create_line(x - self.brush_size, y, x + self.brush_size, y, fill=self.color)

    def set_color(self, color):
        self.color = color

    def set_brush_size(self, size):
        self.brush_size = size

    def set_brush_shape(self, shape):
        self.brush_shape = shape

    def toggle_eraser_mode(self):
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            canvas_bg_color = self.canvas.cget("bg")
            self.color = canvas_bg_color

    def create_brush_size_buttons(self):
        brush_size_frame = Frame(self.root)
        brush_size_frame.pack()

        sizes = [2, 4, 6, 8, 10, 12, 14, 16]  # Available brush sizes

        for size in sizes:
            button = Button(brush_size_frame, text=str(size), width=2, command=lambda s=size: self.set_brush_size(s))
            button.pack(side="left")

    def create_brush_shape_buttons(self):
        brush_shape_frame = Frame(self.root)
        brush_shape_frame.pack()

        shapes = ["circle", "square"]  # Available brush shapes

        for shape in shapes:
            button = Button(brush_shape_frame, text=shape, width=6, command=lambda s=shape: self.set_brush_shape(s))
            button.pack(side="left")

    def create_eraser_button(self):
        eraser_button = Button(self.root, text="Eraser", width=6, command=self.toggle_eraser_mode)
        eraser_button.pack()

    def set_canvas_size(self, width, height):
        self.canvas.config(width=width, height=height)
        self.canvas_width = width
        self.canvas_height = height

def save_image(canvas):
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        canvas.postscript(file=file_path, colormode='color')

def open_image(canvas):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image = PhotoImage(file=file_path)
        canvas.create_image(0, 0, anchor="nw", image=image)
        canvas.image = image

def change_background_color(canvas, color):
    canvas.configure(bg=color)

if __name__ == "__main__":
    root = Tk()
    app = DrawingApp(root)

    menu = Menu(root)
    root.config(menu=menu)

    file_menu = Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save", command=lambda: save_image(app.canvas))
    file_menu.add_command(label="Open", command=lambda: open_image(app.canvas))

    color_menu = Menu(menu)
    menu.add_cascade(label="Color", menu=color_menu)

    # List of unique colors
    unique_colors = set(["black", "blue", "green", "orange", "pink", "purple", "red", "yellow",
                         "brown", "cyan", "magenta", "gray", "dark blue"])

    for color in unique_colors:
        color_menu.add_command(label=color.capitalize(), command=lambda c=color: app.set_color(c))

    background_menu = Menu(menu)
    menu.add_cascade(label="Background", menu=background_menu)
    background_menu.add_command(label="White", command=lambda: change_background_color(app.canvas, "white"))
    background_menu.add_command(label="Gray", command=lambda: change_background_color(app.canvas, "gray"))
    background_menu.add_command(label="Light Blue", command=lambda: change_background_color(app.canvas, "light blue"))
    background_menu.add_command(label="Light Green", command=lambda: change_background_color(app.canvas, "light green"))
    background_menu.add_command(label="Light Yellow", command=lambda: change_background_color(app.canvas, "light yellow"))
    background_menu.add_command(label="Light Pink", command=lambda: change_background_color(app.canvas, "light pink"))

    options_menu = Menu(menu)
    menu.add_cascade(label="Options", menu=options_menu)

    def change_canvas_size():
        size_str = simpledialog.askstring("Canvas Size", "Enter new width and height separated by a space:")
        try:
            width, height = map(int, size_str.split())
            app.set_canvas_size(width, height)
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

    options_menu.add_command(label="Change Canvas Size", command=change_canvas_size)

    root.mainloop()
