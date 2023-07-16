import tkinter as tk
import random

score = 0
player_dy = 0

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
    #bottom light green hill
    canvas2.create_oval(-50, 415, 550, 600, fill="forest green", outline="forest green")
    # river
    coord = 235, 415, 265, 415, 310, 500, 190, 500
    arc = canvas2.create_polygon(coord, fill="skyblue", outline="skyblue" )


def runrules():
    # Removes the welcome page and displays the rules
    welcomecanvas.pack_forget()
    rules_canvas = tk.Canvas(root, bg="skyblue")
    rules_canvas.pack(fill=tk.BOTH, expand=True)
    rules = 'Press <Space> to jump over obstacles'
    rulesmessage = tk.Message(rules_canvas, text=rules,  font=("Comic Sans MS", 16))
    rulesmessage.pack(pady=(120, 60))
    # Creates the go back button on the rules page
    goback_button = tk.Button(rules_canvas, text='Go Back',  font=("Comic Sans MS", 14), width=15, height=2, command=lambda: [rules_canvas.pack_forget(),
                                                                                       welcomecanvas.pack(fill=tk.BOTH, expand=True),
                                                                                       opening_bg(welcomecanvas)])
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
        global score
        if check_collision():
            canvas.unbind("<space>")
            canvas.create_text(75, 200, text="╭━━━╮", fill="lemon chiffon")
            canvas.create_text(75, 215, text="┃╭━╮┃", fill="lemon chiffon")
            canvas.create_text(75, 230, text="┃┃╱╰╋", fill="lemon chiffon")
            canvas.create_text(75, 245, text="┃┃╭━┫", fill="lemon chiffon")
            canvas.create_text(75, 260, text="┃╰┻━┃", fill="lemon chiffon")
            canvas.create_text(75, 275, text="╰━━━┻", fill="lemon chiffon")
            canvas.create_text(125, 230, text="━━┳", fill="lemon chiffon")
            canvas.create_text(125, 245, text="╭╮┃", fill="lemon chiffon")
            canvas.create_text(125, 260, text="╭╮┃", fill="lemon chiffon")
            canvas.create_text(125, 275, text="╯╰┻", fill="lemon chiffon")
            canvas.create_text(165, 230, text="╮╭┳", fill="lemon chiffon")
            canvas.create_text(165, 245, text="╰╯┃", fill="lemon chiffon")
            canvas.create_text(165, 260, text="┃┃┃", fill="lemon chiffon")
            canvas.create_text(165, 275, text="┻┻┻", fill="lemon chiffon")
            canvas.create_text(205, 230, text="━━┳", fill="lemon chiffon")
            canvas.create_text(205, 245, text="┃━┫", fill="lemon chiffon")
            canvas.create_text(205, 260, text="┃━┫", fill="lemon chiffon")
            canvas.create_text(205, 275, text="━━┻", fill="lemon chiffon")
            canvas.create_text(240, 230, text="━━┳", fill="lemon chiffon")
            canvas.create_text(240, 245, text="╭╮┃", fill="lemon chiffon")
            canvas.create_text(240, 260, text="╰╯┣", fill="lemon chiffon")
            canvas.create_text(240, 275, text="━━╯", fill="lemon chiffon")
            canvas.create_text(273, 230, text="╮╭", fill="lemon chiffon")
            canvas.create_text(280, 245, text="╰╯┃", fill="lemon chiffon")
            canvas.create_text(280, 260, text="╮╭┫", fill="lemon chiffon")
            canvas.create_text(280, 275, text="╰╯╰", fill="lemon chiffon")
            canvas.create_text(320, 230, text="━━┳", fill="lemon chiffon")
            canvas.create_text(320, 245, text="┃━┫", fill="lemon chiffon")
            canvas.create_text(320, 260, text="┃━┫", fill="lemon chiffon")
            canvas.create_text(320, 275, text="━━┻", fill="lemon chiffon")
            canvas.create_text(350, 230, text="━╮", fill="lemon chiffon")
            canvas.create_text(350, 245, text="╭╯", fill="lemon chiffon")
            canvas.create_text(345, 260, text="┃", fill="lemon chiffon")
            canvas.create_text(345, 275, text="╯", fill="lemon chiffon")
            canvas.create_text(200, 300, text="Your score was " + str(score), font=("Helvetica", 24),
                               fill="lemon chiffon")
            playagain_button = tk.Button(root, text='Play Again', cursor="exchange", font=("Comic Sans MS", 14),
                                         width=15, height=2, command=lambda: [canvas.pack_forget(),
                                                                              rungame(),
                                                                              playagain_button.pack_forget(),
                                                                              exit_button.pack_forget()])
            playagain_button.pack()
            exit_button = tk.Button(root, text='Exit', cursor="draft_large", font=("Comic Sans MS", 14), width=15,
                                    height=2, command=root.destroy)
            exit_button.pack()
            score = 0
            # reset score to zero after every turn
            return

        for obstacle in obstacles:
            canvas.move(obstacle, -15, 0)  # Move the obstacles faster (adjust the value as desired)
            obstacle_pos = canvas.coords(obstacle)
            # if obstacle is off=-screen, remove it
            if obstacle_pos[2] < 0:
                canvas.delete(obstacle)
                obstacles.remove(obstacle)
                score += 1

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
    global score
    # Create the player
    player_color = random.randint(0, 2)
    if score == 3:
        player = canvas.create_oval(170, 350, 220, 400, fill="blue", outline="white")
        score += 1
    elif player_color == 1:
        player = canvas.create_oval(170, 350, 220, 400, fill="green", outline="white")
    else:
        player = canvas.create_oval(170, 350, 220, 400, fill="black", outline="white")

    # Create a list to store the obstacle objects
    obstacles = []

    # Create the start menu
    start_button = tk.Button(root, text="Start", cursor="draft_large", font=("Comic Sans MS", 14), width=15, height=2, command=start_game)
    start_button.pack()




if __name__ == '__main__':
    # Creates main window for the game, rules, and welcome page canvas
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Mountain Jump Game")


    # Creates the canvas that the homepage(buttons and welcome) will appear on
    welcomecanvas = tk.Canvas(root, bg="skyblue")
    welcomecanvas.pack(fill=tk.BOTH, expand=True)
    opening_bg(welcomecanvas)

    # Creates the title on homepage
    d = tk.Label(welcomecanvas, text="Welcome to Mountain Jump!", font=("Comic Sans MS", 18))
    d.pack(pady=(160, 60))

    # Creates start game button
    strt_button = tk.Button(welcomecanvas, text='Start Game', cursor="draft_large", font=("Comic Sans MS", 14) , width=15, height=2, bg="skyblue", command=lambda: [rungame(),
                                                                                         welcomecanvas.pack_forget()])
    strt_button.pack()

    # Creates see rules button
    rules_button = tk.Button(welcomecanvas, text='See Rules', cursor="draft_large", width=15, height=2, font=("Comic Sans MS", 14), command=runrules)
    rules_button.pack(pady=15)

    # code below puts window in middle for user-- if this doesn't happen let me know
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

