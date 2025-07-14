
# Basic Calculator using Tkinter
import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result.set(eval(entry.get()))
        except:
            result.set("Error")
    elif text == "C":
        result.set("")
    else:
        result.set(result.get() + text)

root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8)
result = tk.StringVar()
buttons = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "C", "0", "=", "/"]
for i, b in enumerate(buttons):
    btn = tk.Button(root, text=b, font="Arial 20")
    btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    btn.bind("<Button-1>", click)
root.mainloop()
