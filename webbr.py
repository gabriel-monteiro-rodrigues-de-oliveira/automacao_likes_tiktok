import pyautogui
from time import sleep


def open_webbr(user_webbr):
    sleep(2)
    pyautogui.press('WIN')
    sleep(1)
    pyautogui.write(user_webbr)
    sleep(1)
    pyautogui.press('ENTER')
    return sleep(5)


def open_tt(tt_url):
    pyautogui.hotkey('ALT', 'D')
    sleep(1)
    pyautogui.write(tt_url)
    sleep(1)
    pyautogui.press('ENTER')
    return sleep(5)
