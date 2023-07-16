import tkinter as tk

def create_game_canvas(root):
    # Create the canvas
    canvas = tk.Canvas(root, width=400, height=400, bg="skyblue")
    canvas.pack()

    # Set the focus on the canvas to receive key events
    canvas.focus_set()

    # the start of background art scene below
    # Sun
    canvas.create_oval(240, 50, 140, 155, fill="gold", outline="gold")
    # rightside,top,left,bottom,

    # clouds
    # middle_lefttop_cloud
    canvas.create_oval(200, 68, 120, 75, fill="papaya whip", outline="papaya whip")
    # rightside,top,left,bottom
    # middle_rightbottom_cloud
    canvas.create_oval(230, 73, 155, 80, fill="papaya whip", outline="papaya whip")
    # middle_leftbottom_cloud
    canvas.create_oval(190, 73, 125, 80, fill="papaya whip", outline="papaya whip")
    # middle_bottom_cloud
    canvas.create_oval(210, 76, 140, 85, fill="papaya whip", outline="papaya whip")
    # left_bottom_cloud
    canvas.create_oval(65, 58, -20, 65, fill="papaya whip", outline="papaya whip")
    # left_middle_cloud
    canvas.create_oval(45, 50, -20, 61, fill="papaya whip", outline="papaya whip")
    # left_middletop_cloud
    canvas.create_oval(30, 45, -20, 54, fill="papaya whip", outline="papaya whip")
    # left_top_cloud
    canvas.create_oval(20, 40, -20, 50, fill="papaya whip", outline="papaya whip")
    # right_middle_cloud
    canvas.create_oval(390, 35, 310, 42, fill="papaya whip", outline="papaya whip")
    # right_bottom_cloud
    canvas.create_oval(410, 30, 330, 38, fill="papaya whip", outline="papaya whip")
    # right_top_cloud
    canvas.create_oval(410, 25, 350, 35, fill="papaya whip", outline="papaya whip")

    # Light Purple Mountains
    # *******************************
    # lightpurp_mostleft_mount
    canvas.create_polygon(120, 410, -100, 410, 30, 50, fill="#8F8FBC", outline="#8F8FBC")
    # right corner, left corner, top corner^^
    # lightpurp_left_mount
    canvas.create_polygon(250, 410, 50, 410, 150, 100, fill="#8F8FBC", outline="#8F8FBC")
    # lightpurp_leftslope_mount
    canvas.create_polygon(250, 410, 100, 410, 180, 150, fill="#8F8FBC", outline="#8F8FBC")
    # lightpurp_middle_mount
    canvas.create_polygon(330, 410, 150, 410, 238, 120, fill="#8F8FBC", outline="#8F8FBC")
    # lightpurp_right_mount
    canvas.create_polygon(410, 410, 230, 410, 310, 70, fill="#8F8FBC", outline="#8F8FBC")
    # lightpurp_mostright_mount
    canvas.create_polygon(460, 410, 260, 410, 360, 135, fill="#8F8FBC", outline="#8F8FBC")

    # Mid Purple Mountains
    # *******************************
    # midpurp_left1_mount
    canvas.create_polygon(120, 410, -20, 410, 55, 125, fill="darkslateblue", outline="darkslateblue")
    # right corner, left corner, top corner^^
    # midpurp_left2_mount
    canvas.create_polygon(230, 410, 30, 410, 120, 190, fill="darkslateblue", outline="darkslateblue")
    # midpurp_left2_slope2_mount
    canvas.create_polygon(250, 410, 70, 410, 160, 230, fill="darkslateblue", outline="darkslateblue")
    # midpurp_left3_mount
    canvas.create_polygon(310, 410, 180, 410, 240, 160, fill="darkslateblue", outline="darkslateblue")
    # midpurp_middle_mount
    canvas.create_polygon(340, 410, 230, 410, 280, 120, fill="darkslateblue", outline="darkslateblue")
    # midpurp_right_mount
    canvas.create_polygon(370, 410, 250, 410, 310, 200, fill="darkslateblue", outline="darkslateblue")
    # midpurp_mostright_mount
    canvas.create_polygon(435, 410, 280, 410, 350, 250, fill="darkslateblue", outline="darkslateblue")
    # the end of background art scene
    return canvas