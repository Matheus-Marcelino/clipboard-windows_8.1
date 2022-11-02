from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file('conf.kv', encoding='utf8')


class Interface(App):
    def build(self):
        return GUI


Interface().run()
