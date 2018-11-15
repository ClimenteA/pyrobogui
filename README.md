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
Describing the parameters:<br>

Put either:<br>

* image - path to image (.png recomended)

<br>or<br>

* x - coodonate number
* y - coordonate number

<br>Additionally you have:<br>

* offsetUp - make action up from the center specified
* offsetDown - make action down from the center specified
* offsetLeft - make action down from the center specified
* offsetRight - make action down from the center specified
* imageError - raise error when this image is found in screen while waiting for the image needed
* timeout - if the seconds specified passes without the image needed to appear then raise error

<br>
These parameters are available for the bellow functions too:
<br>

* rightClick
* doubleClick
* hover
* dragTo

<br>

```
robo.write (text, image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=1800)
```
<br>
Where:
<br>

* text - the string to write on the center of the image or the coordinates specified


scrollUp
scrollDown
scrollLeft
scrollRight












