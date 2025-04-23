# gui.py
import tkinter as tk
from tkinter import messagebox
from datetime import date
from database import add_habit, get_habits, mark_completed, get_completions

class HabitTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Habit Tracker")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f4f8")

        self.habit_name_entry = tk.Entry(root, width=30)
        self.habit_name_entry.pack(pady=10)

        add_button = tk.Button(root, text="Add Habit", command=self.add_habit_ui)
        add_button.pack()

        self.habits_frame = tk.Frame(root, bg="#f0f4f8")
        self.habits_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.refresh_habits()

    def add_habit_ui(self):
        name = self.habit_name_entry.get().strip()
        if name:
            add_habit(name)
            self.habit_name_entry.delete(0, tk.END)
            self.refresh_habits()
        else:
            messagebox.showwarning("Input Error", "Please enter a habit name.")

    def refresh_habits(self):
        for widget in self.habits_frame.winfo_children():
            widget.destroy()

        habits = get_habits()
        for habit in habits:
            habit_id, name = habit
            frame = tk.Frame(self.habits_frame, bg="#ffffff", pady=5, padx=5, relief=tk.RIDGE, bd=2)
            frame.pack(padx=10, pady=5, fill=tk.X)

            label = tk.Label(frame, text=name, anchor="w", width=20)
            label.pack(side=tk.LEFT)

            completed_today = str(date.today()) in get_completions(habit_id)
            status = "✅" if completed_today else "❌"
            status_label = tk.Label(frame, text=status, width=3)
            status_label.pack(side=tk.RIGHT)

            complete_button = tk.Button(
                frame, text="Mark Done", command=lambda h_id=habit_id: self.complete_habit_ui(h_id)
            )
            complete_button.pack(side=tk.RIGHT)

    def complete_habit_ui(self, habit_id):
        mark_completed(habit_id)
        self.refresh_habits()
