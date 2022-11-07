import tkinter as tk
from get import get_ctrl_c
from threading import Thread
from keyboard import add_hotkey, wait


def config_window_state() -> None:
    def state() -> None:
        if WINDOW.state() == 'iconic':    
            WINDOW.state(newstate='normal')
        elif WINDOW.state() == 'normal':
            WINDOW.state(newstate='iconic')

    add_hotkey('win + v', state)
    wait()


def card() -> None:
    pass


def disable_event() -> None:
    card = tk.Text(WINDOW, height=5, width=40, fg='white', bg='black')
    card.insert('end', chars=get_ctrl_c())
    card.grid(column=0, row=0, padx=WIDTH/10, pady=5)


#def move_window(event: any) -> None:
#    WINDOW.geometry('+{0}+{1}'.format(event.x_root, event.y_root))


WINDOW = tk.Tk()
WINDOW.resizable(width=False, height=False)
WINDOW.title("Area de Transferência")
WINDOW.protocol("WM_DELETE_WINDOW", disable_event)
WINDOW.state(newstate='iconic')
FRM_WIDTH = WINDOW.winfo_rootx() - WINDOW.winfo_x()
TITLEBAR_HEIGHT = WINDOW.winfo_rooty() - WINDOW.winfo_y()
HEIGHT = 500
WIDTH = 400
X = WINDOW.winfo_screenwidth() // 2 - (WIDTH + 2 * FRM_WIDTH) // 2
Y = WINDOW.winfo_screenheight() // 2 - (HEIGHT + TITLEBAR_HEIGHT + FRM_WIDTH) // 2
WINDOW.geometry(f'{WIDTH}x{HEIGHT}+{X}+{Y}')
WINDOW.wm_attributes('-topmost' , True)
#WINDOW.wm_attributes('-toolwindow', True)
WINDOW['bg'] = "#1e1e1e"

"""
title_bar = tk.LabelFrame(WINDOW, bg='#1e1e1e', font='Arial 12', relief='raised',
                          height=25, text='Area de Transferência',
                          labelanchor='n')
title_bar.pack(expand=0, fill='x')
title_bar.bind('<B1-Motion>', move_window)
"""


tk.Label(text=card())
#WINDOW.after(2, card)

Thread(target=config_window_state).start()
WINDOW.mainloop()
