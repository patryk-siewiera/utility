import pyperclip
import validators
import youtube_dl
import time


def press_to_continue():
    input("\n\nPress Enter to Exit...\n")


def clipboard_validate_url():
    clipboard = pyperclip.paste()
    validators_message = "\nUrl validation check: \t\t"
    validations_bool = validators.url(clipboard)

    if validations_bool:
        print(validators_message, validations_bool)
        print('return LINK.. \n')
        return clipboard
    else:
        print(validators_message, validations_bool)
        print("\n>> WRONG LINK <<\nEXIT")
        press_to_continue()
        exit()


def ydl_download(link):
    ydl_opts = {
        'outtmpl': 'C:/Users/workp/Desktop/%(title)s -- %(uploader)s.%(ext)s',
        'noplaylist': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    press_to_continue()


ydl_download(clipboard_validate_url())
