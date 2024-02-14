import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

entry = tk.Entry(root, font=("Helvetica", 20))
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for button_text, row, col in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Helvetica", 18), relief="ridge", borderwidth=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)

root.mainloop()
