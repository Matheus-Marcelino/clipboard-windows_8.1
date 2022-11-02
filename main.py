from get import get_ctrl_c
from keyboard import add_hotkey, wait


def init() -> None:
    print(get_ctrl_c())


add_hotkey('win + v', init)
wait()