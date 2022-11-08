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
    def create_card() -> None:
        linha = 0
        
        for c in copy:
            card = tk.Text(WINDOW, width=40, height=9)
            card.grid(column=0, row=linha, padx=WIDTH/10, pady=3)
            card.insert(index='end', chars=c)
            linha += 1
            WINDOW.update_idletasks()

    copy, tamanho = get_ctrl_c(), len(get_ctrl_c())
    ident = 0
    print(copy)

    if tamanho != ident:
        create_card()
        ident += 1

    WINDOW.after(5000, card)


def new_event_delete() -> None:
    WINDOW.state(newstate='iconic')


#def move_window(event: any) -> None:
#    WINDOW.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

WINDOW = tk.Tk()
WINDOW['bg'] = "#1e1e1e"
WINDOW.title("Area de Transferência")
WINDOW.resizable(width=False, height=False)
#WINDOW.protocol("WM_DELETE_WINDOW", new_event_delete)
WINDOW.wm_attributes('-topmost' , True)
WINDOW.wm_attributes('-toolwindow' , True)
#WINDOW.state(newstate='iconic')
WINDOW.rowconfigure(0, weight=0)

HEIGHT = 500
WIDTH = 400
X = WINDOW.winfo_screenwidth() // 2 - (WIDTH + 2) // 2
Y = WINDOW.winfo_screenheight() // 2 - HEIGHT // 2
WINDOW.geometry(f'{WIDTH}x{HEIGHT}+{X}+{Y}')

#WINDOW.wm_attributes('-toolwindow', True)


"""
title_bar = tk.LabelFrame(WINDOW, bg='#1e1e1e', font='Arial 12', relief='raised',
                          height=25, text='Area de Transferência',
                          labelanchor='n')
title_bar.pack(expand=0, fill='x')
title_bar.bind('<B1-Motion>', move_window)
"""

tk.Label(text=card())

Thread(target=config_window_state).start()
WINDOW.update()
WINDOW.mainloop()
