# import pyautogui
import pyperclip


def remove_special_chars():
    clp = pyperclip.paste()
    clp = str(clp)
    clp = clp.splitlines()
    clp = " ".join(clp)
    clp = clp.replace('Ŝ', 'z')
    pyperclip.copy(clp)


remove_special_chars()
