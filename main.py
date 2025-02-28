from tkinter.filedialog import *
import tkinter as tk

canvas = tk.Tk()
canvas.geometry('320x320')
canvas.title('Quick Notepad')
canvas.config(bg = '#c8d3e3')
top = tk.Frame(canvas)
top.pack(padx = 10, pady = 5, anchor= 'nw')


# Button commands--------------------------------
def saveFile():
    new_entry = asksaveasfile(mode = 'w',defaultextension='.diary', filetypes=(('diary file', '.diary'),('All Files', '*.*')))
    if new_entry is None:
        return
    text = str(text_space.get('1.0','end'))
    new_entry.write(text)
    new_entry.close()

def openFile():
    file = askopenfile(mode = 'r',defaultextension='.diary', filetypes=(('diary file', '*.diary'),('All Files', '*.*')))
    if file is not None:
        content = file.read()
        text_space.insert('insert', content) # untab

def clearFile():
    text_space.delete('1.0', 'end')


# Open button -----------------------------------
button_open = tk.Button(canvas, text = 'Open', bg = '#95a7c1', command = openFile)
button_open.pack(in_ = top,side='left')

# Save Button -----------------------------------
button_save = tk.Button(canvas, text = 'Save', bg = '#95a7c1', command = saveFile)
button_save.pack(in_ = top, side='left')

# Clear Button-----------------------------------
button_clear= tk.Button(canvas, text = 'Clear', bg = '#95a7c1', command = clearFile)
button_clear.pack(in_ = top, side='left')

text_space = tk.Text(canvas, wrap = 'word', font = ('courier new', 15))
text_space.pack(padx = 10, pady = 5, expand = True, fill = 'both')

canvas.mainloop()