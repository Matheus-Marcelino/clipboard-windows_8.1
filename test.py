import tkinter as tk
import tkinter.ttk as ttk

class App(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self.create_text()

    def create_text(self):
        self.textbox = tk.Text(self.master, height = 10, width = 79, wrap = 'word')
        self.textbox.insert('end', chars='CUZINHO GOSTOSO')
        vertscroll = ttk.Scrollbar(self.master)
        vertscroll.config(command=self.textbox.yview)
        self.textbox.config(yscrollcommand=vertscroll.set)
        self.textbox.grid(column=0, row=0)
        vertscroll.grid(column=1, row=0, sticky='NS')

root = tk.Tk()
app = App(root)
root.mainloop()