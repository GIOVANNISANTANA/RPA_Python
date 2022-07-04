import pyautogui 
import time

pyautogui.hotkey("win", "d")
pyautogui.hotkey("win", "e")
time.sleep(0.2)
pyautogui.press("f4")
pyautogui.hotkey("ctrl", "a") 
pyautogui.write("imagens")
pyautogui.press("enter")
time.sleep(0.2)
pyautogui.write("digit")
pyautogui.hotkey("ctrl", "c")
time.sleep(0.2)
pyautogui.hotkey("alt", "f4")
print(pyautogui.position())