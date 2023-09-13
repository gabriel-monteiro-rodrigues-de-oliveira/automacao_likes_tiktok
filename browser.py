import pyautogui
from time import sleep


def open_browser(user_browser):
    pyautogui.press('WIN')
    sleep(1)
    pyautogui.write(user_browser)
    sleep(1)
    pyautogui.press('ENTER')
    return sleep(5)


def open_tiktok(tt_url):
    pyautogui.hotkey('ALT', 'D')
    sleep(1)
    pyautogui.write(tt_url)
    sleep(1)
    pyautogui.press('ENTER')
    return sleep(5)
