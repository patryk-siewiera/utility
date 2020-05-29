import pyperclip
import validators
import youtube_dl
import time


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
        time.sleep(2)
        exit()


def ydl_download(link):
    ydl_opts = {
        'outtmpl': 'C:/Users/workp/Desktop/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


ydl_download(clipboard_validate_url())
