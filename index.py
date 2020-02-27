from tkinter import ttk
from tkinter import *

# Functions
def toggle_full_screen():
    window.attributes('-fullscreen', True)

def undo_full_screen():
    window.geometry('800x400')

# Start window, set title and screensize
window = Tk()
window.title("Flashcard app")
window.geometry('800x400')

# set full screen
# window.attributes('-fullscreen', True)

# open full screen
full_screen_button = Button(window,text="Full Screen Mode", command=toggle_full_screen)
full_screen_button.grid(column=4, row=4)

undo_full_screen = Button(window,text="Exit Screen Mode", command=undo_full_screen)
undo_full_screen.grid(column=1, row=4)

txt = Entry(window,width=10)

txt.grid(column=6, row=6)

window.mainloop()
