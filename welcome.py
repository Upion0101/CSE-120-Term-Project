import tkinter as tk

def opening_bg(canvas2):

    # dark purple mountains left to right
    canvas2.create_rectangle(0, 200, 500, 300, outline="darkslateblue", fill="darkslateblue", width=2)
    canvas2.create_polygon(-150, 200, 0, 50, 50, 200, fill="darkslateblue", outline="darkslateblue")
    canvas2.create_polygon(0, 200, 50, 80, 100, 200, fill="darkslateblue", outline="darkslateblue")
    canvas2.create_polygon(100, 200, 175, 30, 250, 200, fill="darkslateblue", outline="darkslateblue")
    canvas2.create_polygon(230, 200, 280, 60, 330, 200, fill="darkslateblue", outline="darkslateblue")
    canvas2.create_polygon(245, 200, 295, 80, 355, 200, fill="darkslateblue", outline="darkslateblue")
    canvas2.create_polygon(355, 200, 413, 20, 470, 200, fill="darkslateblue", outline="darkslateblue")
    canvas2.create_polygon(450, 200, 500, 60, 550, 200, fill="darkslateblue", outline="darkslateblue")
    # light purple mountains left to right
    canvas2.create_rectangle(0, 205, 500, 500, outline="#8F8FBC", fill="#8F8FBC", width=2)
    canvas2.create_polygon(-30, 205, 20, 100, 70, 205, fill="#8F8FBC", outline="#8F8FBC")
    canvas2.create_polygon(50, 205, 100, 120, 150, 205, fill="#8F8FBC", outline="#8F8FBC")
    canvas2.create_polygon(150, 205, 200, 110, 250, 205, fill="#8F8FBC", outline="#8F8FBC")
    canvas2.create_polygon(180, 205, 230, 90, 280, 205, fill="#8F8FBC", outline="#8F8FBC")
    canvas2.create_polygon(250, 205, 300, 125, 350, 205, fill="#8F8FBC", outline="#8F8FBC")
    canvas2.create_polygon(325, 205, 375, 90, 425, 205, fill="#8F8FBC", outline="#8F8FBC")
    canvas2.create_polygon(405, 205, 477, 90, 550, 205, fill="#8F8FBC", outline="#8F8FBC")
    # sun and clouds
    canvas2.create_oval(40, 30, 85, 75, outline="gold", fill="gold", width=2)
    canvas2.create_oval(0, 50, 50, 55, fill="papaya whip", outline="papaya whip")
    canvas2.create_oval(25, 55, 60, 60, fill="papaya whip", outline="papaya whip")
    canvas2.create_oval(200, 68, 120, 75, fill="papaya whip", outline="papaya whip")
    canvas2.create_oval(130, 72, 240, 78, fill="papaya whip", outline="papaya whip")
    canvas2.create_oval(300, 72, 370, 78, fill="papaya whip", outline="papaya whip")
    canvas2.create_oval(310, 70, 380, 72, fill="papaya whip", outline="papaya whip")
    # first green dark green hill
    canvas2.create_oval(-50, 300, 150, 578, fill="dark green", outline="dark green")
    # overlap green hill on left
    canvas2.create_oval(50, 320, 250, 478, fill="dark green", outline="dark green")
    # right green hill
    canvas2.create_oval(230, 578, 550, 320, fill="dark green", outline="dark green")
    # bottom light green hill
    canvas2.create_oval(-50, 415, 550, 600, fill="forest green", outline="forest green")
    # river
    coord = 235, 415, 265, 415, 310, 500, 190, 500
    arc = canvas2.create_polygon(coord, fill="skyblue", outline="skyblue")




