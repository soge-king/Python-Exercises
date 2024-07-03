import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk, Style

# Constants for the timer durations
Worktime = 25 * 60  # 25 minutes
Shorttime = 5 * 60  # 5 minutes
Longtime = 15 * 60  # 15 minutes

class PomodoroTimer:
    def __init__(self):
        # Initialize the main window
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.title("Pomodoro Timer")
        
        # Apply the 'simplex' style from ttkbootstrap
        self.style = Style("simplex")
        self.style.theme_use()  # This line may not be necessary; 'Style' already applies the theme

        # Label to display the timer
        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 40))
        self.timer_label.pack(pady=20)

        # Start button
        self.start_button = ttk.Button(self.root, text="START", command=self.start_timer)
        self.start_button.pack(pady=5)

        # Stop button, initially disabled
        self.stop_button = ttk.Button(self.root, text="STOP", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        # Initial settings for timer states
        self.work_time = Worktime
        self.break_time = Shorttime
        self.is_work_time = True
        self.pomodoros_completed = 0
        self.is_running = False

        # Start the Tkinter main loop
        self.root.mainloop()

    def start_timer(self):
        # Disable the start button and enable the stop button when timer starts
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()

    def stop_timer(self):
        # Enable the start button and disable the stop button when timer stops
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                # Decrement work time if currently in work period
                self.work_time -= 1
                if self.work_time == 0:
                    # Switch to break time if work time is up
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = Longtime if self.pomodoros_completed % 4 == 0 else Shorttime
                    messagebox.showinfo("Break Time", "Take a long break!" if self.pomodoros_completed % 4 == 0 else "Take a short break!")
            else:
                # Decrement break time if currently in break period
                self.break_time -= 1
                if self.break_time == 0:
                    # Switch to work time if break time is up
                    self.is_work_time = True
                    self.work_time = Worktime
                    messagebox.showinfo("Work Time", "Get back to work!")
            
            # Update the timer display
            minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))

            # Call update_timer again after 1 second
            self.root.after(1000, self.update_timer)

# Create an instance of the PomodoroTimer class to start the application
PomodoroTimer()
