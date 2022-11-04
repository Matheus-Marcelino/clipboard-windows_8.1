import tkinter as tk
import threading
import get
from keyboard import add_hotkey, wait

def show_window() -> None:
    def maximizar() -> None:
       WINDOW.state(newstate='normal')
    
    add_hotkey('win + v', maximizar)


def hide_window() -> None:
    WINDOW.state(newstate='iconic')


def disable_event() -> None:
    pass


def display() -> None:
    card = tk.Text(WINDOW, height=10, width=30, fg='white')
    card.insert('end', chars=get.get_ctrl_c())
    card.pack()
    
    
WINDOW = tk.Tk()
WINDOW.resizable(width=False, height=False)
WINDOW.title("Criptografador")
WINDOW.resizable(False, False)
WINDOW.geometry('600x600')
WINDOW.wm_attributes('-topmost', True)
#WINDOW.protocol("WM_DELETE_WINDOW", disable_event)
#WINDOW.state(newstate='iconic')
WINDOW.wm_maxsize(600, 600)
WINDOW['bg'] = "black"

tk.Label(text=display())
WINDOW.after(2, display)

threading.Thread(target=show_window).start()
WINDOW.mainloop()
