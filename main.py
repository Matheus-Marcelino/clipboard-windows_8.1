from keyboard import add_hotkey, wait
from get import get_ctrl


def init():
    print(get_ctrl())


add_hotkey('win + v', init)
wait()