import pyautogui
import pyperclip

clp = pyperclip.paste()
clp = str(clp)

print("\t\t***\t\tclipboard before\n\n", clp, "\n\n")

clp = clp.splitlines()
clp = " ".join(clp)
clp = clp.replace('Ŝ','z')

print("\t\t###\t\tclipboard AFTER\n\n", clp, "\n\n")

pyperclip.copy(clp)

