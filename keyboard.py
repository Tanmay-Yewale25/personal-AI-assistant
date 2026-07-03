import pyautogui
import time

class keyboard:
    def __init__(self):
        pass
    
    def next(self):
        pyautogui.hotkey("right")
        
    def previous(self):
        pyautogui.hotkey("left")
        
    def enter(self):
        pyautogui.hotkey("Enter")
        
    def multitasking_2(self):
        pyautogui.hotkey("win", "z")
        time.sleep(0.2)
        pyautogui.press("1")
        
    def multitasking_3(self):
        pyautogui.hotkey("win", "z")
        time.sleep(0.2)
        pyautogui.press("2")
        
    def multitasking_4(self):
        pyautogui.hotkey("win", "z")
        time.sleep(0.2)
        pyautogui.press("6")
        
        