import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import  Scrollbar as ttk_scrollbar
from get import get_ctrl_c, copy_ctrl_c, delete
from threading import Thread
from keyboard import add_hotkey, wait
delete()


def config_window_state() -> None:
    def state() -> None:
        if WINDOW.state() == 'iconic':    
            WINDOW.state(newstate='normal')
        elif WINDOW.state() == 'normal':
            WINDOW.state(newstate='iconic')

    add_hotkey('win + v', state)
    wait()


def element_func() -> None:
    global ident

    def limpar() -> None:
        global ident

        copy.clear()
        ident = 0
        for widget in frame_main.winfo_children():
            widget.destroy()

    def create_Card() -> None: 
        def copiar(marcador: int) -> None:
            copy_ctrl_c(copy[marcador])

        def botao_copy(marcador: int) -> None:
            botao = tk.Button(frame_main, text='Copiar', fg='white', command = lambda: copiar(marcador), pady=1,
                      bg='#2d2d2d', anchor='n', width=44)    
            botao.grid(column=0, row=line_button, sticky='s')

        line, line_button = 1, 2

        for marcador in range(0, len(copy)):
            card = tk.Text(frame_main, width=40, height=6, autoseparators=True, blockcursor=True, bg='#424242', fg='white')
            card.grid(column=0, row=line, padx=WIDTH/17, pady=3)
            card.insert(index='end', chars=copy[marcador])
            botao_copy(marcador)
            card.configure(selectbackground=card.cget('bg'), inactiveselectbackground=card.cget('bg'), state='disabled')
            frame_main.update_idletasks()
            line += 2
            line_button += 2

        canvas['scrollregion'] = (0,0,0, frame_main.winfo_reqheight())

    copy, tamanho = get_ctrl_c(), len(get_ctrl_c())

    botao_limpar = tk.Button(frame_main, text='Limpar', fg='white', command= limpar,
                      bg='#2d2d2d', anchor='n', width=44)    
    botao_limpar.grid(column=0, row=0, sticky='n', pady=6)

    
    if ident != tamanho:
        ident += 1
        create_Card()

    frame_main.after(2000, element_func)


def new_event_delete() -> None:
    WINDOW.state(newstate='iconic')


WINDOW = tk.Tk()
WINDOW['bg'] = '#1e1e1e'
WINDOW.config(borderwidth=0)
WINDOW.title("Area de Transferência -- beta 1.0")
WINDOW.resizable(width=False, height=False)
WINDOW.wm_attributes('-topmost' , True)
WINDOW.call('wm', 'iconphoto', WINDOW._w, tk.PhotoImage(file='icon/trasnfer.png'))
WINDOW.protocol("WM_DELETE_WINDOW", new_event_delete)
WINDOW.state(newstate='iconic')
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

frame_main = tk.Frame(canvas, bg='#1e1e1e')
canvas.create_window((0, 0), window=frame_main, anchor='nw')

WINDOW.grid_rowconfigure(0, weight=1)

ident = 0  # variavel de controle para a criação de card
element_func()
canvas['scrollregion'] = (0,0,0, 500)

Thread(target=config_window_state).start()
WINDOW.mainloop()
