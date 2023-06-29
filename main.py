import tkinter as tk
import random


def runrules():
    welcomecanvas.pack_forget()
    rules_canvas = tk.Canvas(root, width=400, height=300)
    rules_canvas.pack()
    rules = 'This is where rules will display'
    rulesmessage = tk.Message(rules_canvas, text=rules)
    rulesmessage.pack()
    goback_button = tk.Button(rules_canvas, text='Go Back', width=25, command=lambda: [rules_canvas.pack_forget(),
                                                                                       welcomecanvas.pack()])
    goback_button.pack(padx=10, pady=10)


def rungame():
    def jump(event):
        """Makes the player jump."""
        canvas.move(player, 0, -75)  # Move the player up
        canvas.after(300, fall)  # Schedule the player to fall after a longer delay

    def fall():
        """Makes the player fall down after a jump."""
        canvas.move(player, 0, 75)  # Move the player down

    def check_collision():
        """Checks if there is a collision between the player and any of the obstacles."""
        player_pos = canvas.coords(player)
        for obstacle in obstacles:
            obstacle_pos = canvas.coords(obstacle)
            if player_pos[1] < obstacle_pos[3] and player_pos[3] > obstacle_pos[1]:  # compare vertical overlap
                if player_pos[2] > obstacle_pos[0] and player_pos[0] < obstacle_pos[2]:  # compare horizntal overlap
                    return True
        return False

    def create_obstacle():
        """Creates a triangle obstacle at the bottom of the canvas."""
        x = 400
        y_base = canvas.winfo_height()
        triangle_height = 50  # Adjust the triangle height as desired
        obstacle = canvas.create_polygon(
            x, y_base - triangle_height,  # Tip
            x - 20, y_base,  # Left corner
            x + 20, y_base,  # Right corner
            fill="red"
        )
        obstacles.append(obstacle)

    def update_game():
        """Updates the game state."""
        if check_collision():
            canvas.unbind("<space>")
            canvas.create_text(200, 200, text="Game Over", font=("Helvetica", 24), fill="red")
            return

        for obstacle in obstacles:
            canvas.move(obstacle, -15, 0)  # Move the obstacles faster (adjust the value as desired)
            obstacle_pos = canvas.coords(obstacle)
            # if obstacle is off=-screen, remove it
            if obstacle_pos[2] < 0:
                canvas.delete(obstacle)
                obstacles.remove(obstacle)

        if random.randint(1, 10) == 1:
            create_obstacle()

        canvas.after(50, update_game)  # Adjust the delay between game updates (lower value for faster updates)

    def start_game():
        """Starts the game by hiding the start menu and starting the game loop."""
        start_button.pack_forget()
        canvas.bind("<space>", jump)
        update_game()

    # Create the canvas
    canvas = tk.Canvas(root, width=400, height=400, bg="skyblue")
    canvas.pack()

    # Set the focus on the canvas to receive key events
    canvas.focus_set()

    # the start of background art scene below
    # Sun
    canvas.create_oval(240, 50, 140, 155, fill="gold", outline="gold")
    # rightside,top,left,bottom,

    # Light Purple Mountains
    # *******************************
    # lightpurp_mostleft_mount
    canvas.create_polygon(130, 410, -100, 410, 30, 50, fill="#8F8FBC", outline="#8F8FBC")
    # right corner, left corner, top corner^^
    # lightpurp_right_mount
    canvas.create_polygon(250, 410, 50, 410, 150, 100, fill="#8F8FBC", outline="#8F8FBC")
    # lightpurp_rightslope_mount
    canvas.create_polygon(250, 410, 100, 410, 180, 150, fill="#8F8FBC", outline="#8F8FBC")
    # lightpurp_middle_mount
    canvas.create_polygon(330, 410, 150, 410, 238, 120, fill="#8F8FBC", outline="#8F8FBC")
    # lightpurp_left_mount
    canvas.create_polygon(410, 410, 230, 410, 310, 70, fill="#8F8FBC", outline="#8F8FBC")

    # Mid Purple Mountains
    # *******************************
    # midpurp_left1_mount
    canvas.create_polygon(230, 410, 50, 410, 130, 170, fill="darkslateblue", outline="darkslateblue")
    # right corner, left corner, top corner^^
    # midpurp_left1_slope_mount
    canvas.create_polygon(230, 410, 30, 410, 115, 190, fill="darkslateblue", outline="darkslateblue")
    # 3 mountains on right info below
    # midpurp_left_mount
    canvas.create_polygon(310, 410, 180, 410, 240, 140, fill="darkslateblue", outline="darkslateblue")
    # midpurp_middle_mount
    canvas.create_polygon(340, 410, 230, 410, 280, 150, fill="darkslateblue", outline="darkslateblue")
    # midpurp_right_mount
    canvas.create_polygon(370, 410, 250, 410, 310, 200, fill="darkslateblue", outline="darkslateblue")

    # Dark Purple Mountains
    # *******************************
    # darkpurp_mostleft_mount
    canvas.create_polygon(100, 410, -60, 410, 30, 150, fill="#10104E", outline="#10104E")
    # right corner, left corner, top corner^^
    # darkpurp_left_mount
    canvas.create_polygon(130, 410, 2, 410, 66, 170, fill="#10104E", outline="#10104E")
    # darkpurp_lefttrec
    canvas.create_rectangle(80, 410, 190, 260, fill="#10104E", outline="#10104E")
    # leftside, bottom, rightside, top^^
    # darkpurp_middle_mount
    canvas.create_polygon(250, 410, 150, 410, 200, 100, fill="#10104E", outline="#10104E")
    # darkpurp_middle_rightslope_mount
    canvas.create_polygon(300, 410, 200, 410, 200, 350, fill="#10104E", outline="#10104E")
    # darkpurp_rightrect
    canvas.create_rectangle(340, 410, 200, 310, fill="#10104E", outline="#10104E")
    # rightside, bottom, leftside, top^^
    # darkpurp_rightslope_mount
    canvas.create_polygon(300, 410, 200, 410, 200, 250, fill="#10104E", outline="#10104E")
    # darkpurp_right_mount
    canvas.create_polygon(405, 410, 310, 410, 405, 20, fill="#10104E", outline="#10104E")
    # the end of background art scene

    # Create the player
    player = canvas.create_oval(170, 350, 220, 400, fill="blue", outline="blue")

    # Create a list to store the obstacle objects
    obstacles = []

    # Create the start menu
    start_button = tk.Button(root, text="Start", command=start_game)
    start_button.pack()

    # Run the GUI event loop


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Mountain Jump Game")
    welcomecanvas = tk.Canvas(root, width=400, height=400)
    welcomecanvas.pack()

    d = tk.Label(welcomecanvas, text="Welcome to Mountain Jump!", font=('Arial', 18))
    d.pack(padx=10, pady=10)

    strt_button = tk.Button(welcomecanvas, text='Start Game', width=25, command=lambda: [rungame(),
                                                                                         welcomecanvas.pack_forget()])
    strt_button.pack()

    rules_button = tk.Button(welcomecanvas, text='See Rules', width=25, command=runrules)
    rules_button.pack()

    # code below puts window in middle for user-- if this doesnt happen let me know
    width = 500  # Width
    height = 500  # Height

    screen_width = root.winfo_screenwidth()  # Width of the screen
    screen_height = root.winfo_screenheight()  # Height of the screen

    # Calculate Starting A and B coordinates for Window
    a = (screen_width / 2) - (width / 2)
    b = (screen_height / 2) - (height / 2)

    root.geometry('%dx%d+%d+%d' % (width, height, a, b))
    # End of the code to center window for user

    root.mainloop()
