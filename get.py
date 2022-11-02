from clipboard import paste

lista_ctrl_c = []

def get_ctrl() -> (list|str):
    global lista_ctrl_c

    excecoes = ['\n', '\t', '\r', "\'", '\"','\a', '\b','\\']
    ctrl_c = paste()
    
    for c in excecoes:
        if c in ctrl_c:
            if c == '\n':
                ctrl_c = ctrl_c.replace(c, ' ')
                continue
            ctrl_c = ctrl_c.replace(c, '')
    
    if not ctrl_c in lista_ctrl_c:
        lista_ctrl_c.append(ctrl_c)
    
    if lista_ctrl_c == None:
        pass
    else:
        return lista_ctrl_c
