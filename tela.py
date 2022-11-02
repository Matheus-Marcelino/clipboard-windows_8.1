import tkinter as tk
from keyboard import add_hotkey, wait

key = True


def ativador() -> None:
    global key
    
    if key is True:
        add_hotkey('win + v', minimizar)
        key = False
    else:
        add_hotkey('win + v', maximizar)
        key = True
    print(key)
    

def disable_event() -> None:
    pass


WINDOW = tk.Tk()
WINDOW.resizable(width=False, height=False)
WINDOW.title("Criptografador")
WINDOW.resizable(False, False)
WINDOW.geometry('600x600')
WINDOW.wm_attributes('-topmost', True)
#WINDOW.protocol("WM_DELETE_WINDOW", disable_event)
WINDOW.wm_maxsize(600, 600)
WINDOW['bg'] = "black"


def maximizar() -> None:
    WINDOW.state(newstate='normal')


def minimizar() -> None:
    WINDOW.state(newstate='iconic')

    
ativador()
tk.Text()
WINDOW.mainloop()
