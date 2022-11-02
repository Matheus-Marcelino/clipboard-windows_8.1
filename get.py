from clipboard import paste

lista_ctrl_c = []

def get_ctrl() -> list:
    if not paste() in lista_ctrl_c:
        lista_ctrl_c.append(paste())
    return lista_ctrl_c
