# Feito por -- Matheus Marcelino Lopes - DevMarcelino
# Finalizado: 10/11/22 ás 18:01

from os import path
from shutil import rmtree
from clipboard import paste, copy

token_list_ctrl_c = []

def get_ctrl_c() -> (list | None):
    global token_list_ctrl_c

    ctrl_c = paste()

    if not ctrl_c in token_list_ctrl_c and ctrl_c != '':
        token_list_ctrl_c.append(ctrl_c)

    if token_list_ctrl_c == None:
        pass
    else:
        return token_list_ctrl_c


def copy_ctrl_c(text: str) -> None:
    copy(text)


def clear_ctrl_c() -> None:
    global token_list_ctrl_c

    token_list_ctrl_c.clear()


def delete() -> None:
    if path.exists('__pycache__'):
        rmtree('__pycache__')
