import tkinter as tk
import random


score = 0
player_dy = 0

def runrules():
    # Removes the welcome page and displays the rules
    welcomecanvas.pack_forget()
    rules_canvas = tk.Canvas(root, width=400, height=300)
    rules_canvas.pack()
    rules = 'Press <Space> to jump over obstacles'
    rulesmessage = tk.Message(rules_canvas, text=rules)
    rulesmessage.pack()
    # Creates the go back button on the rules page
    goback_button = tk.Button(rules_canvas, text='Go Back', width=25, command=lambda: [rules_canvas.pack_forget(),
                                                                                       welcomecanvas.pack()])
    goback_button.pack(padx=10, pady=10)




def rungame():
    def check_collision():
        """Checks if there is a collision between the player and any of the obstacles."""
        player_bbox = canvas.bbox(player)
        for obstacle in obstacles:
            obstacle_bbox = canvas.bbox(obstacle)
            if player_bbox[2] >= obstacle_bbox[0] and player_bbox[0] <= obstacle_bbox[2] and \
                    player_bbox[3] >= obstacle_bbox[1] and player_bbox[1] <= obstacle_bbox[3]:
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

    def jump(event):
        """Makes the player jump."""
        global player_dy
        player_dy = -7  # Adjust the jump height as desired
        canvas.move(player, 0, -75)  # Move the player up
        canvas.after(400, fall)  # Schedule the player to fall after a longer delay

    def fall():
        """Makes the player fall down after a jump."""
        global player_dy
        player_pos = canvas.coords(player)
        canvas.move(player, 0, player_dy)
        player_dy += 1  # Adjust the fall speed as desired

        if player_pos[3] >= canvas.winfo_height():
            canvas.move(player, 0, canvas.winfo_height() - player_pos[3])
            player_dy = 0

        canvas.after(200, fall)  # Schedule the next fall after a delay

    def update_game():
        """Updates the game state."""

        if check_collision():
            canvas.unbind("<space>")
            canvas.create_text(200, 200, text="Game Over", font=("Helvetica", 24), fill="red")
            playagain_button = tk.Button(root, text='Play Again', width=25, command=lambda: [canvas.pack_forget(),
                                                                                             rungame(),
                                                                                             playagain_button.pack_forget(),
                                                                                             exit_button.pack_forget()])
            playagain_button.pack()
            exit_button = tk.Button(root, text='Exit', width=25, command=root.destroy)
            exit_button.pack()
            return

        for obstacle in obstacles:
            canvas.move(obstacle, -15, 0)  # Move the obstacles faster (adjust the value as desired)
            obstacle_pos = canvas.coords(obstacle)
            # if obstacle is off=-screen, remove it
            if obstacle_pos[2] < 0:
                canvas.delete(obstacle)
                obstacles.remove(obstacle)
                global score
                score +=1
                print(score)

        if random.randint(1, 10) == 1:
            create_obstacle()
        canvas.move(player, 0, player_dy)
        canvas.after(50, update_game)  # Adjust the delay between game updates (lower value for faster updates)

    def start_game():
        """Starts the game by hiding the start menu and starting the game loop."""

        player_velocity = [0]  # Store player's velocity as a list

        start_button.pack_forget()
        canvas.bind("<space>", jump)
        fall()
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

    # Create the player
    player = canvas.create_oval(170, 350, 220, 400, fill="blue", outline="white")

    # Create a list to store the obstacle objects
    obstacles = []

    # Create the start menu
    start_button = tk.Button(root, text="Start", command=start_game)
    start_button.pack()

    # Run the GUI event loop


if __name__ == '__main__':
    # Creates main window for the game, rules, and welcome page canvas
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Mountain Jump Game")

    # Creates the canvas that the homepage(buttons and welcome) will appear on
    welcomecanvas = tk.Canvas(root, width=400, height=400)
    welcomecanvas.pack()

    # Creates the title on homepage
    d = tk.Label(welcomecanvas, text="Welcome to Mountain Jump!", font=('Arial', 18))
    d.pack(pady=40)

    # Creates start game button
    strt_button = tk.Button(welcomecanvas, text='Start Game', width=25, command=lambda: [rungame(),
                                                                                         welcomecanvas.pack_forget()])
    strt_button.pack(pady=5)

    # Creates see rules button
    rules_button = tk.Button(welcomecanvas, text='See Rules', width=25, command=runrules)
    rules_button.pack(pady=5)

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
