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

# Sun
canvas.create_oval(30, 40, 90, 100, fill="yellow", outline="orange")

# Doghouse
canvas.create_rectangle(380, 280, 470, 350, fill="brown")
canvas.create_polygon(370, 280, 425, 235, 480, 280, fill="darkred")

# Doghouse door
canvas.create_oval(405, 305, 445, 350, fill="black")

# Small white dog
canvas.create_oval(390, 320, 420, 345, fill="white")   # body
canvas.create_oval(410, 310, 435, 335, fill="white")   # head

# Dog ears
canvas.create_polygon(412, 312, 405, 300, 420, 310, fill="white")
canvas.create_polygon(430, 312, 438, 300, 438, 320, fill="white")

# Dog eye
canvas.create_oval(427, 317, 431, 321, fill="black")

# Ground
canvas.create_rectangle(0, 350, 500, 400, fill="green")

# Clouds
canvas.create_oval(100, 50, 150, 80, fill="white", outline="white")
canvas.create_oval(130, 40, 190, 80, fill="white", outline="white")
canvas.create_oval(170, 50, 220, 80, fill="white", outline="white")

canvas.create_oval(300, 60, 350, 90, fill="white", outline="white")
canvas.create_oval(330, 45, 390, 90, fill="white", outline="white")
canvas.create_oval(370, 60, 420, 90, fill="white", outline="white")

# Birds
canvas.create_arc(100, 120, 115, 130, start=0, extent=180, style="arc")
canvas.create_arc(115, 120, 130, 130, start=0, extent=180, style="arc")

canvas.create_arc(320, 130, 335, 140, start=0, extent=180, style="arc")
canvas.create_arc(335, 130, 350, 140, start=0, extent=180, style="arc")

canvas.create_arc(400, 110, 415, 120, start=0, extent=180, style="arc")
canvas.create_arc(415, 110, 430, 120, start=0, extent=180, style="arc")

# Vegetable Garden
canvas.create_rectangle(10, 220, 120, 350, fill="darkgreen")

# Garden fence
for x in range(10, 121, 20):
    canvas.create_rectangle(x, 210, x+5, 350, fill="brown")

canvas.create_line(10, 230, 120, 230, fill="brown", width=4)
canvas.create_line(10, 270, 120, 270, fill="brown", width=4)
canvas.create_line(10, 310, 120, 310, fill="brown", width=4)

# Carrots
for x in [25, 55, 85]:
    canvas.create_polygon(x, 275, x+8, 295, x+16, 275, fill="orange")
    canvas.create_line(x+8, 275, x+3, 265, fill="green", width=2)
    canvas.create_line(x+8, 275, x+12, 263, fill="green", width=2)

# Cabbages
for x, y in [(35, 320), (75, 320), (105, 290)]:
    canvas.create_oval(x, y, x+20, y+18, fill="lightgreen")

# Tomatoes
for x, y in [(25, 245), (60, 250), (95, 240)]:
    canvas.create_oval(x, y, x+15, y+15, fill="red")
    canvas.create_line(x+7, y, x+7, y-10, fill="green", width=2)

# Pumpkins
for x, y in [(45, 290), (85, 275)]:
    canvas.create_oval(x, y, x+22, y+18, fill="orange")
    canvas.create_line(x+11, y, x+11, y-6, fill="green", width=3)

root.mainloop()