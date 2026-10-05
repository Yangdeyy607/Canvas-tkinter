import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=400, bg="skyblue")
canvas.pack()

# House
canvas.create_rectangle(150, 200, 350, 350, fill="yellow")

# Roof
canvas.create_polygon(130, 200, 250, 100, 370, 200, fill="red")

# Roof shading
for x in range(150, 351, 20):
    canvas.create_line(x, 200, 250, 100, fill="darkred")

# Door
canvas.create_rectangle(225, 280, 275, 350, fill="brown")

# Windows
canvas.create_rectangle(170, 230, 210, 270, fill="blue")
canvas.create_rectangle(290, 230, 330, 270, fill="blue")

root.mainloop()