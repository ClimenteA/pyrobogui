# pyrobogui
Wrapper around pyautogui - plus some new functions

Main dependencies: pyautogui, pyperclip, opencv-python, numpy

Build on top of pyautogui but with some extra features: <br>
    -timeouts, <br>
    -setup, <br>
    -aproximate match of images, <br>
    -can be oriented to a screen coordonate automation or screen images automation or both

Usage:<br>

```
pip install pyautogui
pip install pyperclip
pip install opencv-python
pip install numpy
pip install pyrobogui

#then

from pyrobogui import robo 
```

### Mouse functions 

<br>

```
robo.click(image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=1800, full_match=False)
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

Scroll functions

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
robo.write (text, image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=1800,full_match=False)
```
<br>
Where:
<br>

* text - the string to write on the center of the image or the coordinates specified

<br>

For a list of key names you can press check pyautogui documentation

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

<br>
Get to coordonates for the images needed.
<br>
You can count images of the same type on the screen from UP to DOWN, and LEFT to RIGHT.

```
robo.imageNeddle(image, imageNr='last') 
```
Useful for casses where you have images that look the same on the screen but they are positioned in different places.
<br>

For example let's say the you have a form with a lot of radio buttons and you want to click on the 5th radio button, you will do:

```
robo.imageNeddle("./img/radio_button.png", 5)
```
Also you the options for imageNr parameter:
* imageNr=5 - returns the specified counted image 
* imageNr='last'
* imageNr='first'
* imageNr='all' - returns a list of image locations


### Wait functions

```
robo.waitColorToAppear(xyrgb, imageError=None, timeout=1800) #ex:robo.waitColorToAppear("100, 200, 255, 255, 255") 
robo.waitColorToDisappear(xyrgb, imageError=None, timeout=1800)
```
* xyrgb - a string like this "100, 200, 255, 255, 255"
* imageError - if this image apprears on screen the function will stop
* timeout - wait for the image to appear a specific number of seconds if that seconds pass then raise error

```
robo.waitImageToAppear(image, imageError=None, timeout=1800, full_match=False)
robo.waitImageToDisappear(image, imageError=None, timeout=1800, full_match=False)
```
* image - image you need on screen
* imageError - stop if this image is found
* timeout - stop if takes too long time
* full_match - by default if will aproximate the image on screen by 70% if you change it to True it will match it 100%

full_match - not on all PC's the rgb colors, image size are the same, they may vary a little; that's way full_match is False by default

<br>

### If you want to see more read the source code of this module it's just one file ;)























































































