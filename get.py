from clipboard import paste

lista_ctrl_c = []

def get_ctrl() -> list:
    global lista_ctrl_c

    excecoes = ['\n', '\t', '\r', "\'", '\"','\a', '\b','\\']
    cola = paste()
    for c in excecoes:
        if c in cola:
            if c == '\n':
                cola = cola.replace(c, ' ')
                continue
            cola = cola.replace(c, '')
    
    if not cola in lista_ctrl_c:
        lista_ctrl_c.append(cola)
        return lista_ctrl_c
