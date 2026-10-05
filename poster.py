import tkinter as tk

root = tk.Tk()
root.title("3D Bhutanese House")
root.geometry("1000x700")

canvas = tk.Canvas(root, width=1000, height=700, bg="skyblue")
canvas.pack()


# =========================================================
# SKY
# =========================================================

# Sun
canvas.create_oval(
    50, 40, 130, 120,
    fill="yellow",
    outline="orange",
    width=3
)

# Sun rays
for x1, y1, x2, y2 in [
    (90, 25, 90, 5),
    (90, 135, 90, 155),
    (35, 80, 15, 80),
    (145, 80, 165, 80),
    (50, 40, 35, 25),
    (130, 40, 145, 25),
    (50, 120, 35, 135),
    (130, 120, 145, 135)
]:
    canvas.create_line(
        x1, y1, x2, y2,
        fill="orange",
        width=3
    )


# =========================================================
# CLOUDS
# =========================================================

def cloud(x, y):

    canvas.create_oval(
        x, y + 15,
        x + 55, y + 45,
        fill="white",
        outline="white"
    )

    canvas.create_oval(
        x + 30, y,
        x + 90, y + 45,
        fill="white",
        outline="white"
    )

    canvas.create_oval(
        x + 65, y + 15,
        x + 120, y + 45,
        fill="white",
        outline="white"
    )


cloud(200, 55)
cloud(650, 70)


# =========================================================
# BIRDS
# =========================================================

def bird(x, y):

    canvas.create_arc(
        x, y,
        x + 20, y + 15,
        start=0,
        extent=180,
        style="arc",
        width=2
    )

    canvas.create_arc(
        x + 20, y,
        x + 40, y + 15,
        start=0,
        extent=180,
        style="arc",
        width=2
    )


bird(330, 100)
bird(390, 130)
bird(760, 115)
bird(820, 80)


# =========================================================
# MOUNTAINS
# =========================================================

# Far mountains
canvas.create_polygon(
    0, 350,
    150, 210,
    280, 350,
    fill="lightgray",
    outline="gray"
)

canvas.create_polygon(
    180, 350,
    370, 180,
    560, 350,
    fill="darkgray",
    outline="gray"
)

canvas.create_polygon(
    500, 350,
    700, 190,
    900, 350,
    fill="lightgray",
    outline="gray"
)

# Snow caps
canvas.create_polygon(
    330, 215,
    370, 180,
    410, 215,
    390, 205,
    375, 220,
    360, 205,
    fill="white",
    outline="white"
)

canvas.create_polygon(
    660, 220,
    700, 190,
    740, 220,
    720, 210,
    705, 225,
    690, 210,
    fill="white",
    outline="white"
)


# =========================================================
# GROUND
# =========================================================

canvas.create_rectangle(
    0, 350,
    1000, 700,
    fill="forestgreen",
    outline="forestgreen"
)


# =========================================================
# FLOWER FUNCTION
# =========================================================

def flower(x, y, petal_color):

    # Stem
    canvas.create_line(
        x, y + 15,
        x, y + 55,
        fill="green",
        width=3
    )

    # Leaves
    canvas.create_oval(
        x - 15, y + 30,
        x, y + 42,
        fill="lightgreen",
        outline="green"
    )

    canvas.create_oval(
        x, y + 38,
        x + 15, y + 50,
        fill="lightgreen",
        outline="green"
    )

    # Petals
    canvas.create_oval(
        x - 15, y,
        x, y + 15,
        fill=petal_color
    )

    canvas.create_oval(
        x + 10, y,
        x + 25, y + 15,
        fill=petal_color
    )

    canvas.create_oval(
        x - 3, y - 10,
        x + 12, y + 5,
        fill=petal_color
    )

    canvas.create_oval(
        x - 3, y + 10,
        x + 12, y + 25,
        fill=petal_color
    )

    # Center
    canvas.create_oval(
        x - 2, y + 3,
        x + 12, y + 17,
        fill="yellow",
        outline="orange"
    )


# =========================================================
# FLOWER GARDEN
# =========================================================

canvas.create_rectangle(
    30, 450,
    230, 610,
    fill="darkgreen",
    outline="brown",
    width=4
)

# Garden rows
for y in [490, 540, 590]:

    canvas.create_line(
        35, y,
        225, y,
        fill="saddlebrown",
        width=3
    )

flower(65, 470, "red")
flower(120, 500, "pink")
flower(175, 465, "purple")
flower(80, 550, "yellow")
flower(150, 555, "orange")
flower(200, 525, "pink")


# =========================================================
# MAIN HOUSE
# =========================================================

# ---------------------------------------------------------
# Ground floor front
# ---------------------------------------------------------

canvas.create_rectangle(
    280, 350,
    720, 540,
    fill="#d99b62",
    outline="#4b2a19",
    width=4
)


# Ground floor right side
canvas.create_polygon(
    720, 350,
    790, 375,
    790, 560,
    720, 540,
    fill="#b97845",
    outline="#4b2a19",
    width=4
)


# ---------------------------------------------------------
# Second floor front
# ---------------------------------------------------------

canvas.create_rectangle(
    280, 220,
    720, 350,
    fill="#e0aa70",
    outline="#4b2a19",
    width=4
)


# Second floor right side
canvas.create_polygon(
    720, 220,
    790, 245,
    790, 375,
    720, 350,
    fill="#b97845",
    outline="#4b2a19",
    width=4
)


# =========================================================
# BHUTANESE DECORATIVE BANDS
# =========================================================

# Band between floors
canvas.create_rectangle(
    280, 340,
    720, 355,
    fill="#7b241c",
    outline="#4b2a19"
)

# Gold geometric design
for x in range(300, 700, 45):

    canvas.create_polygon(
        x, 343,
        x + 12, 350,
        x + 24, 343,
        x + 12, 351,
        fill="#d4a017"
    )


# Upper decorative band
canvas.create_rectangle(
    280, 220,
    720, 238,
    fill="#7b241c",
    outline="#4b2a19"
)

for x in range(300, 700, 45):

    canvas.create_polygon(
        x, 222,
        x + 12, 230,
        x + 24, 222,
        x + 12, 230,
        fill="#d4a017"
    )


# =========================================================
# CLEAN BHUTANESE ROOF
# =========================================================

# Main large roof
canvas.create_polygon(
    220, 225,
    500, 85,
    780, 225,
    735, 245,
    500, 125,
    265, 245,
    fill="#7b241c",
    outline="#3d1712",
    width=5
)


# Main roof front panel
canvas.create_polygon(
    265, 220,
    500, 105,
    735, 220,
    500, 145,
    fill="#a83224",
    outline="#5a1712",
    width=3
)


# =========================================================
# ROOF SIDE - 3D DEPTH
# =========================================================

canvas.create_polygon(
    735, 220,
    780, 225,
    825, 255,
    790, 275,
    735, 245,
    fill="#632019",
    outline="#3d1712",
    width=4
)


# Side roof gold edge
canvas.create_line(
    780, 225,
    825, 255,
    790, 275,
    fill="#d4a017",
    width=4
)


# =========================================================
# ROOF GOLD TRIM
# =========================================================

# Left slope
canvas.create_line(
    220, 225,
    500, 85,
    fill="#d4a017",
    width=5
)

# Right slope
canvas.create_line(
    500, 85,
    780, 225,
    fill="#d4a017",
    width=5
)

# Lower roof edge
canvas.create_line(
    220, 225,
    265, 245,
    500, 125,
    735, 245,
    780, 225,
    fill="#d4a017",
    width=5
)


# =========================================================
# ROOF CENTER ORNAMENT
# =========================================================

canvas.create_polygon(
    500, 88,
    525, 102,
    500, 118,
    475, 102,
    fill="#d4a017",
    outline="#5a321d",
    width=2
)

# Roof finial
canvas.create_line(
    500, 88,
    500, 55,
    fill="#5a321d",
    width=4
)

canvas.create_oval(
    490, 43,
    510, 63,
    fill="#d4a017",
    outline="#5a321d",
    width=2
)


# =========================================================
# SIMPLE ROOF PATTERN
# =========================================================

for x in range(290, 711, 40):

    canvas.create_polygon(
        x, 218,
        x + 10, 208,
        x + 20, 218,
        x + 10, 228,
        fill="#d4a017",
        outline="#5a321d"
    )


# =========================================================
# UPPER FLOOR CORRIDOR
# =========================================================

# Balcony floor
canvas.create_polygon(
    270, 350,
    730, 350,
    770, 370,
    310, 370,
    fill="#6b4226",
    outline="#432716",
    width=3
)


# Balcony top rail
canvas.create_line(
    300, 305,
    700, 305,
    fill="#5a321d",
    width=5
)

# Balcony middle rail
canvas.create_line(
    300, 335,
    700, 335,
    fill="#5a321d",
    width=4
)

# Balcony posts
for x in range(300, 701, 40):

    canvas.create_line(
        x, 305,
        x, 350,
        fill="#5a321d",
        width=4
    )


# Simple Bhutanese railing decoration
for x in range(320, 680, 40):

    canvas.create_polygon(
        x, 320,
        x + 10, 310,
        x + 20, 320,
        x + 10, 330,
        fill="#d4a017",
        outline="#5a321d"
    )


# =========================================================
# BHUTANESE WINDOW FUNCTION
# =========================================================

def bhutanese_window(x, y):

    # Wooden outer frame
    canvas.create_rectangle(
        x, y,
        x + 80, y + 65,
        fill="#5a321d",
        outline="#321b10",
        width=4
    )

    # Glass
    canvas.create_rectangle(
        x + 10, y + 12,
        x + 70, y + 55,
        fill="lightblue",
        outline="#321b10",
        width=3
    )

    # Vertical divider
    canvas.create_line(
        x + 40, y + 12,
        x + 40, y + 55,
        fill="#321b10",
        width=3
    )

    # Small Bhutanese top decoration
    canvas.create_polygon(
        x + 5, y + 12,
        x + 20, y - 8,
        x + 40, y + 12,
        x + 60, y - 8,
        x + 75, y + 12,
        fill="#d4a017",
        outline="#5a321d"
    )


# =========================================================
# WINDOWS
# =========================================================

# Upper floor
bhutanese_window(350, 255)
bhutanese_window(570, 255)

# Ground floor
bhutanese_window(325, 395)
bhutanese_window(595, 395)


# =========================================================
# MAIN DOOR
# =========================================================

# Door frame
canvas.create_rectangle(
    445, 390,
    555, 540,
    fill="#4b2818",
    outline="#29150d",
    width=5
)

# Upper door panel
canvas.create_rectangle(
    460, 405,
    540, 445,
    fill="#8b542f",
    outline="#d4a017",
    width=3
)

# Lower door panel
canvas.create_rectangle(
    460, 455,
    540, 525,
    fill="#8b542f",
    outline="#d4a017",
    width=3
)

# Door diamond design
canvas.create_polygon(
    500, 410,
    520, 425,
    500, 440,
    480, 425,
    fill="#d4a017",
    outline="#5a321d"
)

# Door handle
canvas.create_oval(
    525, 470,
    535, 480,
    fill="#d4a017"
)


# =========================================================
# HOUSE SIDE DECORATION
# =========================================================

for y in [275, 320, 400, 450, 500]:

    canvas.create_line(
        725, y,
        775, y + 15,
        fill="#d4a017",
        width=3
    )


# =========================================================
# FRONT STEPS
# =========================================================

canvas.create_rectangle(
    430, 540,
    570, 555,
    fill="gray",
    outline="black"
)

canvas.create_rectangle(
    415, 555,
    585, 570,
    fill="gray",
    outline="black"
)


# =========================================================
# DOGHOUSE
# =========================================================

# Body
canvas.create_rectangle(
    760, 520,
    900, 620,
    fill="#9b5a32",
    outline="#4a2816",
    width=4
)

# Roof
canvas.create_polygon(
    740, 520,
    830, 450,
    920, 520,
    fill="#7b241c",
    outline="#4a1712",
    width=4
)

# Roof trim
canvas.create_line(
    740, 520,
    830, 450,
    920, 520,
    fill="#d4a017",
    width=3
)

# Door
canvas.create_oval(
    795, 555,
    865, 625,
    fill="#291a12",
    outline="#160d09",
    width=3
)


# =========================================================
# CUTE WHITE DOG
# =========================================================

# Body
canvas.create_oval(
    850, 555,
    925, 600,
    fill="white",
    outline="gray",
    width=2
)

# Head
canvas.create_oval(
    900, 525,
    960, 580,
    fill="white",
    outline="gray",
    width=2
)

# Ears
canvas.create_polygon(
    905, 535,
    895, 510,
    920, 525,
    fill="white",
    outline="gray"
)

canvas.create_polygon(
    940, 530,
    955, 505,
    958, 540,
    fill="white",
    outline="gray"
)

# Eyes
canvas.create_oval(
    920, 540,
    927, 547,
    fill="black"
)

canvas.create_oval(
    943, 540,
    950, 547,
    fill="black"
)

# Nose
canvas.create_oval(
    931, 550,
    941, 558,
    fill="black"
)

# Mouth
canvas.create_arc(
    930, 550,
    945, 565,
    start=180,
    extent=180,
    style="arc"
)

# Tail
canvas.create_arc(
    900, 555,
    950, 610,
    start=270,
    extent=180,
    style="arc",
    width=5
)

# Legs
canvas.create_rectangle(
    860, 585,
    875, 615,
    fill="white",
    outline="gray"
)

canvas.create_rectangle(
    895, 585,
    910, 615,
    fill="white",
    outline="gray"
)


# =========================================================
# TREES
# =========================================================

def tree(x, y):

    # Trunk
    canvas.create_rectangle(
        x, y,
        x + 30, y + 100,
        fill="saddlebrown",
        outline="#4a2816"
    )

    # Leaves
    canvas.create_oval(
        x - 35, y - 55,
        x + 65, y + 30,
        fill="darkgreen",
        outline="green"
    )

    canvas.create_oval(
        x - 15, y - 90,
        x + 70, y - 20,
        fill="forestgreen",
        outline="green"
    )


tree(80, 330)
tree(900, 350)


# =========================================================
# FLOWERS AROUND HOUSE
# =========================================================

flower(260, 580, "red")
flower(300, 610, "yellow")
flower(700, 600, "pink")
flower(735, 570, "purple")
flower(940, 630, "orange")


# =========================================================
# STONE PATH
# =========================================================

for x, y in [
    (470, 580),
    (490, 600),
    (510, 620),
    (530, 640)
]:

    canvas.create_oval(
        x, y,
        x + 35, y + 18,
        fill="lightgray",
        outline="gray"
    )


# =========================================================
# FENCE
# =========================================================

for x in range(0, 260, 30):

    canvas.create_rectangle(
        x, 630,
        x + 8, 690,
        fill="saddlebrown",
        outline="#4a2816"
    )

canvas.create_line(
    0, 645,
    260, 645,
    fill="saddlebrown",
    width=5
)

canvas.create_line(
    0, 670,
    260, 670,
    fill="saddlebrown",
    width=5
)


# =========================================================
# GRASS DETAILS
# =========================================================

for x in range(250, 1000, 35):

    canvas.create_line(
        x, 690,
        x + 5, 675,
        fill="darkgreen",
        width=2
    )


# =========================================================
# RUN PROGRAM
# =========================================================

root.mainloop()