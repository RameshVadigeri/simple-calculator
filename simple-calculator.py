import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry box
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=8, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", relief=tk.RAISED)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", on_click)

root.mainloop()
