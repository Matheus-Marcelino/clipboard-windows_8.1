from time import sleep
from get import get_ctrl_c
from keyboard import add_hotkey, wait

def init():
    get_ctrl_c()
    return True

while True:
    a = add_hotkey('win + v', init)
    print(a)
    sleep(1)
    