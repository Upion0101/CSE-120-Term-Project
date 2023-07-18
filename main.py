import tkinter as tk
import random
import time
from welcome import opening_bg
from game_canvas import create_game_canvas

score = 0
player_dy = 0
obstacle_frequency = 1000  # Initial obstacle frequency (1 obstacle per second)
max_obstacle_frequency = 500  # Maximum obstacle frequency (0.5 obstacles per second)
last_obstacle_time = 0
jump_height = -10
fall_speed = 1
def runrules():
    # Removes the welcome page and displays the rules
    welcomecanvas.pack_forget()
    rules_canvas = tk.Canvas(root, bg="skyblue")
    rules_canvas.pack(fill=tk.BOTH, expand=True)
    rules = 'Press <Space> to jump over obstacles'
    rulesmessage = tk.Message(rules_canvas, text=rules, font=("Comic Sans MS", 16))
    rulesmessage.pack(pady=(120, 60))
    # Creates the go back button on the rules page
    goback_button = tk.Button(
        rules_canvas,
        text='Go Back',
        font=("Comic Sans MS", 14),
        width=15,
        height=2,
        cursor= "left_side",
        command=lambda: [rules_canvas.pack_forget(), welcomecanvas.pack(fill=tk.BOTH, expand=True),
                         opening_bg(welcomecanvas)],
    )
    goback_button.pack(padx=10, pady=10)

def rungame():
    start_time = time.time()
    last_obstacle_time = start_time

    def check_collision():
        """Checks if there is a collision between the player and any of the obstacles."""
        player_bbox = canvas.bbox(player)
        #makes the hiboxes smaller
        player_hitbox = [
            player_bbox[0] + 10,
            player_bbox[1] + 10,
            player_bbox[2] - 10,
            player_bbox[3] - 10
        ]
        for obstacle in obstacles:
            obstacle_bbox = canvas.bbox(obstacle)
            obstacle_hitbox = [
                obstacle_bbox[0] + 10,
                obstacle_bbox[1] + 10,
                obstacle_bbox[2] - 10,
                obstacle_bbox[3] - 10
            ]
            if (
                    player_hitbox[2] >= obstacle_hitbox[0] and
                    player_hitbox[0] <= obstacle_hitbox[2] and
                    player_hitbox[3] >= obstacle_hitbox[1] and
                    player_hitbox[1] <= obstacle_hitbox[3]
            ):
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
            fill="red",
        )
        obstacles.append(obstacle)

    def jump(event):
        """Makes the player jump."""
        global player_dy
        player_pos = canvas.coords(player)
        if player_pos[3] == canvas.winfo_height():
            player_dy = jump_height
            canvas.move(player, 0, player_dy)


    def fall():
        """Makes the player fall down after a jump."""
        global player_dy
        player_pos = canvas.coords(player)
        canvas.move(player, 0, player_dy)
        player_dy += fall_speed

        if player_pos[3] >= canvas.winfo_height():
            canvas.move(player, 0, canvas.winfo_height() - player_pos[3])
            player_dy = 0

        canvas.after(20, fall)  # Schedule the next fall after a delay

    def update_game():
        """Updates the game state."""
        global score, obstacle_frequency, last_obstacle_time
        current_time = time.time()
        elapsed_time = current_time - start_time

        if check_collision():
            canvas.unbind("<space>")
            canvas.create_text(
                200,
                230,
                text="G a m e o v e r",
                fill="lemon chiffon",
                font=("Comic Sans MS", 30),
            )
            canvas.create_text(
                190,
                280,
                text="Your score is ",
                font=("Comic Sans MS", 20),
                fill="lemon chiffon",
            )
            canvas.create_text(
                275,
                280,
                text=" ͟ ͟",
                font=("Comic Sans MS", 20),
                fill="lemon chiffon",
            )
            canvas.create_text(
                275,
                280,
                text="" + str(score),
                font=("Comic Sans MS", 20),
                fill="lemon chiffon",
            )
            playagain_button = tk.Button(
                root,
                text="Play Again",
                cursor="exchange",
                font=("Comic Sans MS", 14),
                width=15,
                height=2,
                command=lambda: [
                    canvas.pack_forget(),
                    rungame(),
                    playagain_button.pack_forget(),
                    exit_button.pack_forget(),
                ],
            )
            playagain_button.pack()
            exit_button = tk.Button(
                root,
                text="Exit",
                font=("Comic Sans MS", 14),
                width=15,
                height=2,
                command=root.destroy,
            )
            exit_button.pack()
            score = 0
            # reset score to zero after every turn
            return

        for obstacle in obstacles:
            canvas.move(obstacle, -15, 0)  # Move the obstacles faster (adjust the value as desired)
            obstacle_pos = canvas.coords(obstacle)
            # if obstacle is off-screen, remove it
            if obstacle_pos[2] < 0:
                canvas.delete(obstacle)
                obstacles.remove(obstacle)
                score += 1

        if elapsed_time - last_obstacle_time > obstacle_frequency / 1000:
            create_obstacle()
            last_obstacle_time = elapsed_time

            # Gradually reduce obstacle frequency until it reaches the maximum
            if obstacle_frequency > max_obstacle_frequency:
                obstacle_frequency -= 10

        canvas.move(player, 0, player_dy)
        canvas.after(50, update_game)  # Adjust the delay between game updates (lower value for faster updates)

    def start_game():
        """Starts the game by hiding the start menu and starting the game loop."""

        start_button.pack_forget()
        canvas.bind("<space>", jump)
        fall()
        update_game()

    # Create the canvas
    canvas = create_game_canvas(root)

    global score
    # player color change
    player_color = random.randint(0, 2)
    if player_color == 0:
        player = canvas.create_oval(
            170, 350, 220, 400, fill="blue", outline="white"
        )
    elif player_color == 1:
        player = canvas.create_oval(
            170, 350, 220, 400, fill="green", outline="white"
        )
    else:
        player = canvas.create_oval(
            170, 350, 220, 400, fill="black", outline="white"
        )

    # Create a list to store the obstacle objects
    obstacles = []

    # Create the start menu
    start_button = tk.Button(
        root,
        text="Start",
        font=("Comic Sans MS", 14),
        width=15,
        height=2,
        command=start_game,
    )
    start_button.pack()


if __name__ == "__main__":
    # Creates main window for the game, rules, and welcome page canvas
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Mountain Jump Game")
    # makes window unable to be resized by user
    root.resizable(False, False)

    # Creates the canvas that the homepage(buttons and welcome) will appear on
    welcomecanvas = tk.Canvas(root, bg="skyblue")
    welcomecanvas.pack(fill=tk.BOTH, expand=True)
    opening_bg(welcomecanvas)

    # Creates the title on homepage
    d = tk.Label(
        welcomecanvas,
        text="Welcome to Mountain Jump!",
        font=("Comic Sans MS", 18),
    )
    d.pack(pady=(160, 60))

    # Creates start game button
    strt_button = tk.Button(
        welcomecanvas,
        text="Start Game",
        font=("Comic Sans MS", 14),
        width=15,
        height=2,
        bg="skyblue",
        command=lambda: [rungame(), welcomecanvas.pack_forget()],
    )
    strt_button.pack()

    # Creates see rules button
    rules_button = tk.Button(
        welcomecanvas,
        text="See Rules",
        width=15,
        height=2,
        font=("Comic Sans MS", 14),
        command=runrules,
    )
    rules_button.pack(pady=15)

    # code below puts window in middle for user-- if this doesn't happen let me know
    width = 500  # Width
    height = 500  # Height

    screen_width = root.winfo_screenwidth()  # Width of the screen
    screen_height = root.winfo_screenheight()  # Height of the screen

    # Calculate Starting A and B coordinates for Window
    a = (screen_width / 2) - (width / 2)
    b = (screen_height / 2) - (height / 2)

    root.geometry("%dx%d+%d+%d" % (width, height, a, b))
    # End of the code to center window for user

    root.mainloop()
