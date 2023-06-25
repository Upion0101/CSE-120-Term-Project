import tkinter as tk
import random

def runrules():
    welcomecanvas.pack_forget()
    rules_canvas = tk.Canvas(root, width=400, height=300)
    rules_canvas.pack()
    rules = 'This is where rules will display'
    rulesmessage = tk.Message(rules_canvas, text=rules)
    rulesmessage.pack()
    goback_button = tk.Button(rules_canvas, text='Go Back', width=25, command=lambda: [rules_canvas.pack_forget(), welcomecanvas.pack()])
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
               x - 10, y_base,  # Left corner
               x + 10, y_base,  # Right corner
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
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    # Set the focus on the canvas to receive key events
    canvas.focus_set()
    # Create the player
    player = canvas.create_rectangle(180, 350, 220, 400, fill="blue")
    # Create a list to store the obstacle objects
    obstacles = []

    # Create the start menu
    start_button = tk.Button(root, text="Start", command=start_game)
    start_button.pack()

    # Run the GUI event loop


if __name__ =='__main__':
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Jumping Game")
    welcomecanvas = tk.Canvas(root, width=400, height=400)
    welcomecanvas.pack()

    x = tk.Label(welcomecanvas, text="Welcome to Jumping Game!", font=('Arial', 18))
    x.pack(padx=10, pady=10)

    strt_button = tk.Button(welcomecanvas, text='Start Game', width=25, command=lambda: [rungame(), welcomecanvas.pack_forget()])
    strt_button.pack()

    rules_button = tk.Button(welcomecanvas, text='See Rules', width=25, command=runrules)
    rules_button.pack()

    root.mainloop()


