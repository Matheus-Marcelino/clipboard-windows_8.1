from get import get_ctrl_c
from keyboard import add_hotkey, wait

def a():
    print(get_ctrl_c())

add_hotkey('win + v', a)
wait()
