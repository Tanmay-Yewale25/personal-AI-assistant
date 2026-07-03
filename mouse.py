import pyautogui

class Mouse:
    def __init__(self):
        pass

    def move_to(self, x, y):
        pyautogui.moveTo(x, y)

    def click(self, x=None, y=None):
        if x is not None and y is not None:
            pyautogui.click(x, y)
        else:
            pyautogui.click()

    def double_click(self, x=None, y=None):
        if x is not None and y is not None:
            pyautogui.doubleClick(x, y)
        else:
            pyautogui.doubleClick()

    def right_click(self, x=None, y=None):
        if x is not None and y is not None:
            pyautogui.rightClick(x, y)
        else:
            pyautogui.rightClick()

    def scroll(self, clicks):
        pyautogui.scroll(clicks)