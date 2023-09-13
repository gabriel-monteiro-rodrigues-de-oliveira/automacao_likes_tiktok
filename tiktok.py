import pyautogui
from time import sleep


def login_tiktok(user_name, user_password):
    sleep(1)
    enter_button = pyautogui.locateCenterOnScreen('enter_button.png')
    pyautogui.click(enter_button, duration=1)
    sleep(1)

    use_user_name = pyautogui.locateCenterOnScreen('use_user_name.png')
    pyautogui.click(use_user_name, duration=1)
    sleep(1)

    use_phone = pyautogui.locateCenterOnScreen('use_phone.png')
    pyautogui.click(use_phone, duration=1)
    sleep(1)

    pyautogui.write(user_name, interval=0.1)
    sleep(1)

    enter_with_password = pyautogui.locateCenterOnScreen('enter_with_password.png')
    pyautogui.click(enter_with_password, duration=1)
    sleep(1)

    enter_password = pyautogui.locateCenterOnScreen('enter_password.png')
    pyautogui.click(enter_password, duration=1)
    sleep(1)

    pyautogui.write(user_password, interval=0.1)
    sleep(1)

    tabs = 0
    for tabs in range(4):
        pyautogui.press('TAB')
        tabs += 1

    pyautogui.press('ENTER')

    enter_code = pyautogui.locateCenterOnScreen('enter_code.png')
    pyautogui.click(enter_code, duration=1)
    sleep(1)

    user_code = input('Digite o código de 6 dígitos: ')
    pyautogui.write(user_code, interval=0.1)
    sleep(1)

    pyautogui.press('TAB')
    pyautogui.press('TAB')

    return sleep(7)


def search_creator(tt_url, tt_creator):
    pyautogui.hotkey('ALT', 'D')
    sleep(1)
    pyautogui.write(tt_url + tt_creator)
    sleep(1)
    pyautogui.click('ENTER')
    return sleep(5)


def search_first_video():
    videos_text = pyautogui.locateCenterOnScreen('videos_text.png')
    pyautogui.click(videos_text, duration=1)
    sleep(1)
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('ENTER')
    return sleep(5)


def like_videos(likes):
    video = 0
    while video <= likes:
        sleep(2)
        pyautogui.doubleClick()
        pyautogui.press('down')
    return print('Curtidas finalizado.')
