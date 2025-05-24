import tkinter as tk

# State flag
calculator_on = False

def turn_on():
    global calculator_on
    calculator_on = True
    entry.config(state="normal", justify="center")  # Center for Ashim
    entry.delete(0, tk.END)
    entry.insert(0, "Made by Ashim")
    window.after(1500, clear_splash_and_align_right)
    entry.focus_set()

def clear_splash_and_align_right():
    entry.delete(0, tk.END)
    entry.config(justify="right")

def turn_off():
    global calculator_on
    calculator_on = False
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.config(state="disabled")

def toggle_power():
    if calculator_on:
        turn_off()
        power_btn.config(text="ON")
    else:
        turn_on()
        power_btn.config(text="OFF")

def click(event):
    if not calculator_on:
        return
    handle_input(event.widget.cget("text"))

def key_input(event):
    if not calculator_on:
        return
    key = event.keysym
    if key == "Return":
        handle_input("=")
    elif key == "Escape":
        handle_input("C")
    elif key == "BackSpace":
        current = entry.get()
        if current == "Invalid Input":
            entry.delete(0, tk.END)
        else:
            entry.delete(0, tk.END)
            entry.insert(0, current[:-1])
    else:
        char = event.char
        if char in "0123456789+-*/().":
            handle_input(char)

def handle_input(char):
    if not calculator_on:
        return
    current = entry.get()
    if current == "Invalid Input":
        entry.delete(0, tk.END)
        current = ""
    if char == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Invalid Input")
    elif char == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)

# Create main window
window = tk.Tk()
window.title("Ashim's Calculator")
window.geometry("350x550")
window.config(bg="#1e1e2e")

# Entry field (centered temporarily, right-aligned after splash)
entry = tk.Entry(
    window,
    font="Arial 24",
    bg="#282c34",
    fg="white",
    bd=5,
    relief=tk.FLAT,
    justify="right",
    state="disabled"
)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Power Button
power_btn = tk.Button(
    window,
    text="ON",
    font="Arial 12 bold",
    command=toggle_power,
    bg="#ff7f50",
    fg="white",
    bd=0
)
power_btn.pack(pady=(0, 10))

# Bind keyboard keys
window.bind("<Key>", key_input)

# Buttons Layout
buttons = [
    ["(", ")", "C", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

button_color = "#3b3f51"
hover_color = "#50597b"
text_color = "white"

# Create buttons
for row in buttons:
    frame = tk.Frame(window, bg="#1e1e2e")
    frame.pack(expand=True, fill="both")
    for text in row:
        if text != "":
            btn = tk.Button(
                frame,
                text=text,
                font="Arial 18",
                bg=button_color,
                fg=text_color,
                activebackground=hover_color,
                activeforeground="white",
                bd=0
            )
            btn.pack(side="left", expand=True, fill="both")
            btn.bind("<Button-1>", click)
        else:
            spacer = tk.Label(frame, text="", bg="#1e1e2e")
            spacer.pack(side="left", expand=True, fill="both")

# Run the application
window.mainloop()
