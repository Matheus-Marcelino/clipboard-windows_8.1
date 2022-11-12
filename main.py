# Feito por -- Matheus Marcelino Lopes - DevMarcelino
# Finalizado: 10/11/22 ás 18:01

from tkinter import Tk, TclError, messagebox, Frame, Canvas, Button, Text, PhotoImage, Label
from tkinter.ttk import Scrollbar as ttk_scrollbar
from get import get_ctrl_c, copy_ctrl_c, clear_ctrl_c, delete
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


def element_create() -> None:
    global ident, message

    def limpar() -> None:
        global ident, line, line_button

        clear_ctrl_c()
        ident, line, line_button = 0, 1, 2

        for widget in frame_main.winfo_children():
            widget.destroy()

    def create_Card() -> None:
        global line, line_button

        def botao_copy(marcador: str) -> None:
            Button(frame_main, text='Copiar', background='#2e2e2e', fg='white', command=lambda: copy_ctrl_c(marcador),
                   pady=1, bg='#2d2d2d', anchor='n', width=44).grid(column=0, row=line_button, sticky='s')

        # criando um card e seu botão associado
        for _ in range(1):
            card = Text(frame_main, width=40, height=6, autoseparators=True,
                        blockcursor=True, bg='#424242', fg='white')
            card.grid(column=0, row=line, padx=WIDTH/17, pady=3)
            card.insert(index='end', chars=copy[-1])
            botao_copy(copy[-1])
            card.configure(selectbackground=card.cget(
                'bg'), inactiveselectbackground=card.cget('bg'), state='disabled')
            frame_main.update_idletasks()
            line += 2
            line_button += 2

        # exlucindo a mensagem caso ela não saia
        if message.winfo_exists() == 1:
            limpar()

        #atualizando sempre a região do scroll
        canvas['scrollregion'] = (0, 0, 0, frame_main.winfo_reqheight())

    copy, tamanho = get_ctrl_c(), len(get_ctrl_c())

    if len(copy) != 0:
        Button(frame_main, text='Limpar', fg='white', command=limpar,
               bg='#2d2d2d', anchor='n', width=44).grid(column=0, row=0, sticky='n', pady=6)
    else:
        message = Label(frame_main, text='Esperando você copiar algo :)', bg='#1e1e1e',
                    fg='#2e2e2e', font="Bahnschrift 15")
        message.grid(column=0, row=0, sticky='nwes', padx=WIDTH/7, pady=HEIGHT/2.2)

    if ident != tamanho:
        ident += 1
        create_Card()

    frame_main.after(2000, element_create)


def new_event_delete() -> None:
    WINDOW.state(newstate='iconic')


try:
    WINDOW = Tk()
    WINDOW['bg'] = '#1e1e1e'
    # Centralizando a tela ao iniciar
    HEIGHT = int(500)
    WIDTH = int(400)
    X = WINDOW.winfo_screenwidth() // 2 - (WIDTH + 2) // 2
    Y = WINDOW.winfo_screenheight() // 2 - HEIGHT // 2
    WINDOW.geometry(f'{WIDTH}x{HEIGHT}+{X}+{Y}')

    WINDOW.state(newstate='iconic')
    WINDOW.title("Area de Transferência -- beta 3.0")
    WINDOW.resizable(width=False, height=False)
    WINDOW.wm_attributes('-topmost', True)
    try:
        WINDOW.call('wm', 'iconphoto', WINDOW._w,
                    PhotoImage(file='icon/transfer.png'))
    except TclError:
        messagebox.showerror('Image Not Found Error', "A imagem 'transfer.png' "
                             "não pode ser encontrada no\nLocal 'icon/transfer.png' ")
        WINDOW.destroy()
    WINDOW.protocol("WM_DELETE_WINDOW", new_event_delete)

    canvas = Canvas(WINDOW, bg='#1e1e1e')
    canvas.grid(row=0, column=0, sticky='nwes')

    scroll = ttk_scrollbar(WINDOW, orient="vertical", command=canvas.yview)
    scroll.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=scroll.set)

    frame_main = Frame(canvas, bg='#1e1e1e')
    canvas.create_window((0, 0), window=frame_main, anchor='nw')

    WINDOW.grid_rowconfigure(0, weight=1)

    message = Label(frame_main, text='Esperando você copiar algo :)', bg='#1e1e1e',
                    fg='#2e2e2e', font="Bahnschrift 15")
    message.grid(column=0, row=0, sticky='nwes', padx=WIDTH/7, pady=HEIGHT/2.2)

    ident, line, line_button = 0, 1, 2  # variavel de controle para a criação de card
    element_create()
    canvas['scrollregion'] = (0, 0, 0, 500)

    Thread(target=element_create).start()
    Thread(target=config_window_state).start()
    WINDOW.mainloop()
except TclError:
    pass
