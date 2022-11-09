import tkinter as tk
import tkinter.ttk as ttk
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
        linha = 0
        for frase in copy:
            card = tk.Text(frame_text, width=40, height=6, autoseparators=True)
            card.grid(column=0, row=linha, padx=WIDTH/10, pady=3)
            card.insert(index='end', chars=frase)
            frame_text.update_idletasks()
            linha += 1
        canvas['scrollregion'] = (0, 0, frame_text.winfo_reqheight(), frame_text.winfo_reqheight())

    print(get_ctrl_c())
    copy, tamanho = get_ctrl_c(), len(get_ctrl_c())

    if ident != tamanho:
        ident += 1
        create_Card()

    frame_text.after(5000, Card_func)


def new_event_delete() -> None:
    WINDOW.state(newstate='iconic')


WINDOW = tk.Tk()
WINDOW['bg'] = "#1e1e1e"
WINDOW.title("Area de Transferência -- alpha")
WINDOW.resizable(width=False, height=False)
WINDOW.wm_attributes('-topmost' , True)
WINDOW.wm_attributes('-toolwindow' , True)
#WINDOW.protocol("WM_DELETE_WINDOW", new_event_delete)
#WINDOW.state(newstate='iconic')

HEIGHT = int(500)
WIDTH = int(400)
X = WINDOW.winfo_screenwidth() // 2 - (WIDTH + 2) // 2
Y = WINDOW.winfo_screenheight() // 2 - HEIGHT // 2
WINDOW.geometry(f'{WIDTH}x{HEIGHT}+{X}+{Y}')

canvas = tk.Canvas(WINDOW, bg="blue")
canvas.grid(row=0, column=0, sticky=('n', 'w', 'e', 's'))

scrool = ttk.Scrollbar(WINDOW, orient="vertical", command=canvas.yview)
scrool.grid(row=0, column=1, sticky=('n', 's'))
canvas.configure(yscrollcommand=scrool.set)

frame_text = tk.Frame(canvas, bg="grey")
canvas.create_window((0, 0), window=frame_text, anchor='nw', height=HEIGHT)

WINDOW.grid_columnconfigure(0, weight=1)
WINDOW.grid_rowconfigure(0, weight=1)

Card_func()

Thread(target=config_window_state).start()
WINDOW.mainloop()
