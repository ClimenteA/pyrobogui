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

### Mouse functions 

<br>

```
robo.click(image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=1800)
```
<br>
Describing the parameters:
<br>
Put either:
<br>

* image - path to image (.png recomended)

or

* x - coodonate number
* y - coordonate number


Additionally you have:

* offsetUp - make action up from the center specified
* offsetDown - make action down from the center specified
* offsetLeft - make action down from the center specified
* offsetRight - make action down from the center specified
* imageError - raise error when this image is found in screen while waiting for the image needed
* timeout - if the seconds specified passes without the image needed to appear then raise error


These parameters are available for the bellow functions too:

* rightClick
* doubleClick
* hover
* dragTo


```
robo.scrollUp(320)
```

<br>
Instert a number for the functions bellow (scroll is noticeable for values over 120)

* scrollUp
* scrollDown
* scrollLeft
* scrollRight

<br>

### Keyboard functions

```
robo.write (text, image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=1800)
```
<br>
Where:
<br>

* text - the string to write on the center of the image or the coordinates specified

<br>

```
robo.press(keys) # Ex: robo.press("ctrl, c")
```
* keys - the hotkeys you want to press, you can press max 3 keys (ex: robo.press("ctrl, alt, delete"))  

<br>

### Additional functions

Start setup to get the x,y coordinates and RGB color from the screen
Useful when you want to start an automation process based on x,y coodinates(xy positions must be the same each time the process runs!)
```
robo.setup()
```
Wait a number of seconds equivalent to > time.sleep(x) 

```
robo.waitSeconds(5) #wait 5 seconds
```

Get coordinates of the image:

```
robo.getImageLocation(image, full_match=False)
```
* image - image you need to find on screen
* full_match - by default if will reduce the match if not found on screen down to 70%. If you set it to True it will try to find on screen an identical match size, colors etc.


















