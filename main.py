import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import  Scrollbar as ttk_scrollbar
from get import get_ctrl_c, delete
from threading import Thread
from keyboard import add_hotkey, wait
delete()

ident = 0  # variavel de controle para a criação de card


def config_window_state() -> None:
    def state() -> None:
        if WINDOW.state() == 'iconic':    
            WINDOW.state(newstate='normal')
        elif WINDOW.state() == 'normal':
            WINDOW.state(newstate='iconic')

    add_hotkey('win + v', state)
    wait()


def Card_func() -> None:
    global ident
    
    def create_Card() -> None: 
        line_button = 1
        for line, frase in enumerate(copy):
            line - 1
            card = tk.Text(frame_text, width=40, height=6, autoseparators=True, blockcursor=True, bg='#424242')
            card.grid(column=0, row=line, padx=WIDTH/17, pady=3)
            card.insert(index='end', chars=frase)
            card.configure(selectbackground=card.cget('bg'), inactiveselectbackground=card.cget('bg'), state='disabled')
            tk.Button(frame_text, text='Copiar', fg='white', bg='#2d2d2d', anchor='n', width=45).grid(
                column=0, row=line_button, sticky='s')
            frame_text.update_idletasks()
            line_button += 1
            canvas['scrollregion'] = (0,0,0, frame_text.winfo_reqheight())

    copy, tamanho = get_ctrl_c(), len(get_ctrl_c())

    if ident != tamanho:
        ident += 1
        create_Card()
    
    frame_text.after(2000, Card_func)


def new_event_delete() -> None:
    WINDOW.state(newstate='iconic')


WINDOW = tk.Tk()
WINDOW['bg'] = '#1e1e1e'
WINDOW.config(borderwidth=0)
WINDOW.title("Area de Transferência -- alpha")
WINDOW.resizable(width=False, height=False)
WINDOW.wm_attributes('-topmost' , True)
WINDOW.protocol("WM_DELETE_WINDOW", new_event_delete)
#WINDOW.state(newstate='iconic')

HEIGHT = int(500)
WIDTH = int(400)
X = WINDOW.winfo_screenwidth() // 2 - (WIDTH + 2) // 2
Y = WINDOW.winfo_screenheight() // 2 - HEIGHT // 2
WINDOW.geometry(f'{WIDTH}x{HEIGHT}+{X}+{Y}')

canvas = tk.Canvas(WINDOW, bg='#1e1e1e')
canvas.grid(row=0, column=0, sticky='nwes')

scroll = ttk_scrollbar(WINDOW, orient="vertical", command=canvas.yview)
scroll.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=scroll.set)

frame_text = tk.Frame(canvas, bg='#1e1e1e')
canvas.create_window((0, 0), window=frame_text, anchor='nw')

WINDOW.grid_rowconfigure(0, weight=1)
WINDOW.grid_columnconfigure(0, weight=1)

Card_func()
canvas['scrollregion'] = (0,0,0, 500)

Thread(target=config_window_state).start()
WINDOW.mainloop()
