# main.py
import tkinter as tk
from gui import HabitTrackerApp
from database import init_db

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop()
