import tkinter as tk
from get import get_ctrl_c
from threading import Thread
from keyboard import add_hotkey, wait


def show_window() -> None:
    def uepa() -> None:
        if WINDOW.state() == 'iconic':    
            WINDOW.state(newstate='normal')
        elif WINDOW.state() == 'normal':
            WINDOW.state(newstate='iconic')
        
    add_hotkey('win + v', uepa)
    wait()

def disable_event() -> None:
    pass


def display() -> None:
    card = tk.Text(WINDOW, height=10, width=30, fg='white')
    card.insert('end', chars=get_ctrl_c())
    card.pack()
    
    
WINDOW = tk.Tk()
WINDOW.resizable(width=False, height=False)
WINDOW.title("Area de Transferência")
FRM_WIDTH = WINDOW.winfo_rootx() - WINDOW.winfo_x()
TITLEBAR_HEIGHT = WINDOW.winfo_rooty() - WINDOW.winfo_y()
X = WINDOW.winfo_screenwidth() // 2 - (600 + 2 * FRM_WIDTH) // 2
Y = WINDOW.winfo_screenheight() // 2 - (600 + TITLEBAR_HEIGHT + FRM_WIDTH) // 2
WINDOW.geometry(f'{600}x{600}+{X}+{Y}')
WINDOW.wm_attributes('-topmost', True)
WINDOW.protocol("WM_DELETE_WINDOW", disable_event)
WINDOW.state(newstate='iconic')
WINDOW.wm_maxsize(600, 600)
WINDOW['bg'] = "black"

tk.Label(text=display())
#WINDOW.after(2, display)

Thread(target=show_window).start()
WINDOW.mainloop()
