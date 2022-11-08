from os import path
from shutil import rmtree
from clipboard import paste

lista_ctrl_c = []


def get_ctrl_c() -> (list | None):
    global lista_ctrl_c

    ctrl_c = paste()
    
    if not ctrl_c in lista_ctrl_c and ctrl_c != '':
        lista_ctrl_c.append(ctrl_c)

    if lista_ctrl_c == None:
        pass
    else:
        return lista_ctrl_c


def delete() -> None:
    if path.exists('__pycache__'):
        rmtree('__pycache__')

delete()
