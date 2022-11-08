import tkinter as tk
import tkinter.ttk as ttk
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


def Card() -> None:
    def create_Card() -> None:
        linha = 0
        
        for c in copy:
            card.grid(column=0, row=linha, padx=WIDTH/10, pady=3)
            card.insert(index='end', chars=c)
            linha += 1
            WINDOW.update_idletasks()

    print(get_ctrl_c())
    copy, tamanho = get_ctrl_c(), len(get_ctrl_c())
    ident = 0

    if tamanho != ident:
        create_Card()
        ident += 1

    WINDOW.after(5000, card)


def new_event_delete() -> None:
    WINDOW.state(newstate='iconic')


#def move_window(event: any) -> None:
#    WINDOW.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

WINDOW = tk.Tk()
WINDOW['bg'] = "#1e1e1e"
WINDOW.title("Area de Transferência -- alpha")
#WINDOW.resizable(width=False, height=False)
WINDOW.protocol("WM_DELETE_WINDOW", new_event_delete)
WINDOW.wm_attributes('-topmost' , True)
#WINDOW.wm_attributes('-toolwindow' , True)
#WINDOW.state(newstate='iconic')
#WINDOW.rowconfigure(0, weight=0)

HEIGHT = 500
WIDTH = 400
X = WINDOW.winfo_screenwidth() // 2 - (WIDTH + 2) // 2
Y = WINDOW.winfo_screenheight() // 2 - HEIGHT // 2
WINDOW.geometry(f'{WIDTH}x{HEIGHT}+{X}+{Y}')

"""
title_bar = tk.LabelFrame(WINDOW, bg='#1e1e1e', font='Arial 12', relief='raised',
                          height=25, text='Area de Transferência',
                          labelanchor='n')
title_bar.pack(expand=0, fill='x')
title_bar.bind('<B1-Motion>', move_window)
"""
card = tk.Text(WINDOW, width=40, height=6)
Card()

scrollvert = ttk.Scrollbar(WINDOW, orient='vertical')
scrollvert.grid(column=1, row=0, sticky='NS')
scrollvert.config(command=card.yview)

Thread(target=config_window_state).start()
WINDOW.update()
WINDOW.mainloop()
