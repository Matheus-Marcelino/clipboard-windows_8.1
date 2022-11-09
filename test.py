from tkinter import *
import tkinter.filedialog

class homepage:
    def __init__(self):
        inicio = Tk()

        inicio.title("Pena Software")
        inicio.geometry("720x580+100+50")
        inicio['bg'] = '#F2F2F2'
        #inicio.iconbitmap(r'pena.ico')

        #def Open(): 
        #    tkFileDialog.askopenfilename()
        def Quit(): 
            inicio.destroy()

        menubar = Menu(tearoff=False)
        inicio.config(menu=menubar)

        MENUarquivo = Menu(tearoff=False)
        menubar.add_cascade(label="Arquivo", menu=MENUarquivo)
        MENUarquivo.add_command(label="Criar Sorteio",)
        MENUarquivo.add_command(label="Abrir...",)
        MENUarquivo.add_command(label="Editar Sorteios",)
        MENUarquivo.add_separator()
        MENUarquivo.add_command(label="Sair", command=Quit)


        MENUferramentas = Menu(tearoff=False)
        menulang = Menu(tearoff=False)
        menubar.add_cascade(label="Ferramentas", menu=MENUferramentas)

        menulang.add_command(label="Português",)
        menulang.add_command(label="English",)
        MENUferramentas.add_cascade(label="Linguagens", menu=menulang)

        def escuro():
            inicio.configure(background="black")

        def claro():
            inicio.configure(background="light gray")


        menuamb = Menu(tearoff=False)
        menuamb.add_checkbutton(label="Padrão", command=claro)
        menuamb.add_checkbutton(label="Noite...", command=escuro)
        MENUferramentas.add_cascade(label="Ambiente", menu=menuamb)


        MENUajuda = Menu(menubar, tearoff=False)
        MENUajuda.add_command(label="Sobre")
        MENUajuda.add_command(label="Como Usar?",)
        menubar.add_cascade(label="Ajuda", menu=MENUajuda)

        inicio.mainloop()

    def sobre():# uma pequena função "sobre"

        root = Tk()
        root.geometry("240x110+75+75")
        root.title("Sobre")


        texto=("Pena_Software.v0.1_Estável")
        textONlabel = Label(root, text=texto)
        textONlabel.pack()


        lb2 = Label(root, text="Licença Livre")
        lb2.pack()
        
homepage()