# pyrobogui
Wrapper around pyautogui - plus some new functions

Main dependencies: pyautogui, pyperclip, opencv-python, numpy

Build on top of pyautogui but with some extra features: <br>
    -timeouts, <br>
    -setup, <br>
    -aproximate match of images, <br>
    -can be oriented to a screen coordonate automation or screen images automation

Usage:<br>

```
from pyrobogui import Robo #import class Robo

robo = Robo() #create new object
```
Functions you can use:


```
robo.click(image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=1800)
```
Put either:<br>
* image - path to image (.png recomended)
or<br>
* x - coodonate number
* y - coordonate number
Additionally you have:<br>
* offsetUp - make action up from the center specified
* offsetDown - make action down from the center specified
* offsetLeft - make action down from the center specified
* offsetRight - make action down from the center specified
