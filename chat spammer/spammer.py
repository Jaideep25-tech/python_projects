import pyautogui
# pip install pycopy-webbrowser
import webbrowser as wb
# pip install times
import time
wb.open("https://web.whatsapp.com/")
time.sleep(5)

for i in range(10):
    pyautogui.press('F')
    pyautogui.press('O')
    pyautogui.press('L')
    pyautogui.press('L')
    pyautogui.press('O')
    pyautogui.press('W')
    pyautogui.press(' ')
    pyautogui.press('@')
    pyautogui.press('_')
    pyautogui.press('j')
    pyautogui.press('a')
    pyautogui.press('i')
    pyautogui.press('_')
    pyautogui.press('d')
    pyautogui.press('e')
    pyautogui.press('e')
    pyautogui.press('p')
    pyautogui.press('_')
    pyautogui.press('2')
    pyautogui.press('5')
    pyautogui.press('enter')