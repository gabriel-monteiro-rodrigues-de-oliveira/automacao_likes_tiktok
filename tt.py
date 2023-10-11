import pyautogui
from time import sleep


def login_tt(usr_name, usr_passwd):
    sleep(2)
    enter_bttn = pyautogui.locateCenterOnScreen('enter_bttn.png')
    pyautogui.click(enter_bttn, duration=1)
    sleep(3)

    use_usr_name = pyautogui.locateCenterOnScreen('use_usr_phone.png')
    pyautogui.click(use_usr_name, duration=1)
    sleep(1)

    use_phone = pyautogui.locateCenterOnScreen('use_phone.png')
    pyautogui.click(use_phone, duration=1)
    sleep(1)

    pyautogui.write(usr_name, interval=0.1)
    sleep(1)

    enter_with_passwd = pyautogui.locateCenterOnScreen('enter_with_passwd.png')
    pyautogui.click(enter_with_passwd, duration=1)
    sleep(1)

    enter_passwd = pyautogui.locateCenterOnScreen('enter_passwd.png')
    pyautogui.click(enter_passwd, duration=1)
    sleep(1)

    pyautogui.write(usr_passwd, interval=0.1)
    sleep(1)

    tabs = 0
    for tabs in range(4):
        pyautogui.press('TAB')
        tabs += 1

    pyautogui.press('ENTER')

    pyautogui.press('TAB')
    pyautogui.press('TAB')

    pyautogui.hotkey('ALT', 'TAB')
    usr_code = input('Digite o código de 6 dígitos: ')
    pyautogui.hotkey('ALT', 'TAB')
    sleep(1)
    pyautogui.write(usr_code, interval=0.1)
    sleep(1)

    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('ENTER')

    return sleep(7)


def srch_creator(tt_url, tt_creator):
    sleep(3)
    pyautogui.hotkey('ALT', 'TAB')

    tt_com = pyautogui.locateCenterOnScreen('tt_com.png')
    pyautogui.click(tt_com, interval=1)
    sleep(1)

    pyautogui.write(tt_url + '@' + tt_creator)
    sleep(1)

    pyautogui.press('ENTER')
    return sleep(5)


def srch_frst_video():
    videos_txt = pyautogui.locateCenterOnScreen('videos_txt.png')
    pyautogui.click(videos_txt, duration=1)
    sleep(1)
    pyautogui.press('TAB')
    pyautogui.press('TAB')
    pyautogui.press('ENTER')
    return sleep(5)


def like_videos(likes):
    video = 0
    while video < int(likes):
        sleep(2)
        pyautogui.doubleClick()
        pyautogui.press('down')
    return print('Curtidas finalizado.')
