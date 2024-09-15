"""
Doc String:
Full Screen
HumanBenchmark.com
1920x1080
top of site
"""
import win32api, win32con
from PIL import ImageGrab
import os

def screenGrab():
    im = ImageGrab.grab()
    return im

#defining controls
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def react():
    screenGrab()
    s = screenGrab()
    if s.getpixel((503,281)) == (75, 219, 106):
        leftClick()

def main():
    while True:
        react()
 
if __name__ == '__main__':
    main()
