import tkinter as tk
from tkinter import messagebox

class ChessClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Clock")

        # Initialize times (in seconds)
        self.player1_time = 300  # 5 minutes
        self.player2_time = 300

        # Active player (1 or 2)
        self.active_player = 1

        # Timer running flag
        self.running = False

        # Create UI elements
        self.create_widgets()

        # Timer update loop
        self.update_timer()

    def create_widgets(self):
        # Player 1
        self.player1_label = tk.Label(self.root, text="Player 1", font=("Arial", 16))
        self.player1_label.grid(row=0, column=0, pady=10)
        self.player1_timer = tk.Label(self.root, text=self.format_time(self.player1_time), font=("Arial", 24))
        self.player1_timer.grid(row=1, column=0, pady=10)
        self.player1_button = tk.Button(self.root, text="Switch Turn", command=lambda: self.switch_turn(1), state=tk.DISABLED)
        self.player1_button.grid(row=2, column=0, pady=10)

        # Player 2
        self.player2_label = tk.Label(self.root, text="Player 2", font=("Arial", 16))
        self.player2_label.grid(row=0, column=1, pady=10)
        self.player2_timer = tk.Label(self.root, text=self.format_time(self.player2_time), font=("Arial", 24))
        self.player2_timer.grid(row=1, column=1, pady=10)
        self.player2_button = tk.Button(self.root, text="Switch Turn", command=lambda: self.switch_turn(2), state=tk.DISABLED)
        self.player2_button.grid(row=2, column=1, pady=10)

        # Control buttons
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.grid(row=3, column=0, pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_timer)
        self.reset_button.grid(row=3, column=1, pady=10)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def start_timer(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.player1_button.config(state=tk.NORMAL if self.active_player == 1 else tk.DISABLED)
        self.player2_button.config(state=tk.NORMAL if self.active_player == 2 else tk.DISABLED)

    def reset_timer(self):
        self.running = False
        self.player1_time = 300
        self.player2_time = 300
        self.active_player = 1
        self.update_display()
        self.start_button.config(state=tk.NORMAL)
        self.player1_button.config(state=tk.DISABLED)
        self.player2_button.config(state=tk.DISABLED)

    def switch_turn(self, player):
        if self.running and self.active_player == player:
            self.active_player = 2 if player == 1 else 1
            self.player1_button.config(state=tk.NORMAL if self.active_player == 1 else tk.DISABLED)
            self.player2_button.config(state=tk.NORMAL if self.active_player == 2 else tk.DISABLED)

    def update_timer(self):
        if self.running:
            if self.active_player == 1:
                self.player1_time -= 1
                if self.player1_time <= 0:
                    self.running = False
                    messagebox.showinfo("Game Over", "Player 1's time is up!")
            elif self.active_player == 2:
                self.player2_time -= 1
                if self.player2_time <= 0:
                    self.running = False
                    messagebox.showinfo("Game Over", "Player 2's time is up!")
            self.update_display()
        self.root.after(1000, self.update_timer)

    def update_display(self):
        self.player1_timer.config(text=self.format_time(self.player1_time))
        self.player2_timer.config(text=self.format_time(self.player2_time))


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ChessClock(root)
    root