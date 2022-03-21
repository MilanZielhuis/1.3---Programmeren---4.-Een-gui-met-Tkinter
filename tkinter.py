import tkinter as tk

window = tk.Tk()

frame_greeting = tk.Frame(master=window, bg="yellow")
frame_entry = tk.Frame()

greeting = tk.Label(text="Hoi, wie ben jij?")
entry = tk.Entry()

greeting.configure(bg='red', fg='gold', font=("Segoe UI", 8, "bold italic"))
entry.configure(bg='blue', fg='white', font=("Calibri", 8, "bold"))

greeting.pack()
entry.pack()

window.mainloop
