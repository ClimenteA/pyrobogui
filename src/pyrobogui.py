import time
from datetime import datetime, timedelta

try:
    import cv2
    import numpy as np
except:
    # opencv-python not installed

import pyautogui as pag
import pyperclip as clip


class Robo:
    """Build on top of pyautogui but with some extra features: 
    -timeouts, 
    -setup, 
    -aproximate match of images, 
    -can be oriented to a screen coordonate automation or screen images automation """


    def listifyString(self, astring, delimiter=','):
        """Get a list from a string"""
        strListifyed = astring.split(delimiter)
        astringListifyed = [s.strip() for s in strListifyed]
        return astringListifyed


    def getCoord(self, i, offset=False):
        """Get mouse position and color"""
        coord = pag.position()
        rgb = pag.pixel(coord[0], coord[1])                
        if i == 0:
            pass
        else:
            if offset == False:
                print("Step{} -> X:{}, Y:{}, RGB:{}".format(i,coord[0],coord[1],rgb))
        
        #clipvals = str(str(coord)+";"+str(rgb))
        rgb = str(rgb)
        rgb = rgb.replace('(', '')
        rgb = rgb.replace(')', '')
        clipvals = "{}, {}, {}".format(str(coord[0]), str(coord[1]), rgb) 
        clip.copy(clipvals) 
        if offset:
            return coord[0], coord[1]

    def offsetH(self, ix, cx):
        """Get the difference on horozontal plan (left to right)"""
        if ix > cx:
            x = ix - cx 
            print('offsetLeft: ', x)
        elif ix < cx:
            x = cx - ix 
            print('offsetRight: ', x)


    def offsetV(self, iy, cy):
        """Get the difference on vertical plan (up to down)"""
        if iy > cy:
            y = iy - cy
            print('offsetUp: ', y)
        elif iy < cy:
            y = cy - iy
            print('offsetDown: ', y)



    def setup(self):
        """Console interface for getting mouse position and color"""

        print("\n\nPress Enter to get new values for the mouse position. \nType offset to get the distance between 2 points\nType q followed by an Enter to quit setup.\nThis window must remain active!")
        user = ''
        i=0
        while user != 'ok' and user != 'q':
            if user == 'offset':
                coordli = []
                for i in range(2):
                    user = input('\nPress Enter(to get new values), q then Enter(to quit)\n')
                    x, y = self.getCoord(i, offset=True)
                    coordli.append([x, y]) #[[766, 279], [1445, 266]]
                ix, iy = coordli[0][0], coordli[0][1]
                cx, cy = coordli[1][0], coordli[1][1]
                print('values {')
                self.offsetH(ix, cx)
                self.offsetV(iy, cy)
                print("}")
                print('\nPut the values of the offsets listed up in the excel!\n\n')
            else:
                self.getCoord(i)

            user = input('\nPress Enter(to get new values), q then Enter(to quit)\n')
            i += 1  


    def offset(self, x, y, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None):
        """Offset offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None for a given x ,y coordonate"""
        offsetDict = {}

        if offsetUp != None:
            offsetDict['offsetUp'] = int(float(offsetUp))
        if offsetDown != None:
            offsetDict['offsetDown'] = int(float(offsetDown))
        if offsetLeft != None:
            offsetDict['offsetLeft'] = int(float(offsetLeft))
        if offsetRight != None:
            offsetDict['offsetRight'] = int(float(offsetRight))

        for k, v in offsetDict.items():
            if k == 'offsetUp':
                y = y - v
            elif k == 'offsetDown':
                y = y + v
            elif k == 'offsetLeft':
                x = x - v
            elif k == 'offsetRight':
                x = x + v

        return abs(int(x)), abs(int(y))




    def customFilterList(self, neddleli, *args):
        """Filter list by keeping only indexes from args(count starts from 1)"""
        #customFilterList(['1','2','3','4','5'], 3)
        filteredList = []
        for arg in args:
            filteredList.append(neddleli[arg-1])
        return filteredList


    def click(self, image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=30, full_match=False):
        """Clicks by default the center of the image if no offsets are given. 
        Optionally you can set image to greyscale or just insert the x, y coordinates"""
        if image != None:    
            location = self.waitImageToAppear(image, imageError, timeout, full_match)    
            x, y = pag.center(location)
            x, y = self.offset(x, y, offsetUp, offsetDown, offsetLeft, offsetRight)
            pag.click(x, y)
            return x, y
        else:
            x, y = self.offset(x, y, offsetUp, offsetDown, offsetLeft, offsetRight)
            pag.click(x, y)
            return x, y


    # In[5]:


    def rightClick(self, image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=30, full_match=False):
        """Same as click func"""
        if image != None:    
            location = self.waitImageToAppear(image, imageError, timeout, full_match)    
            x, y = pag.center(location)
            x, y = self.offset(x, y, offsetUp, offsetDown, offsetLeft, offsetRight)
            pag.rightClick(x, y)
            return x, y
        else:
            x, y = self.offset(x, y, offsetUp, offsetDown, offsetLeft, offsetRight)
            pag.rightClick(x, y)
            return x, y


    # In[6]:


    def doubleClick(self, image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=30, full_match=False):
        """Same as click func"""
        if image != None:   
            location = self.waitImageToAppear(image, imageError, timeout, full_match)     
            x, y = pag.center(location)
            x, y = self.offset(x, y, offsetUp, offsetDown, offsetLeft, offsetRight)
            pag.doubleClick(x, y)
            return x, y
        else:
            x, y = self.offset(x, y, offsetUp, offsetDown, offsetLeft, offsetRight)
            pag.doubleClick(x, y)
            return x, y


    # In[7]:


    def hover(self, image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=30, full_match=False):
        """Same as click func"""
        if image != None:    
            location = self.waitImageToAppear(image, imageError, timeout, full_match)    
            x, y = pag.center(location)
            x, y = self.offset(x, y, offsetUp, offsetDown, offsetLeft, offsetRight)
            pag.moveTo(x, y)
            return x, y
        else:
            x, y = self.offset(x, y, offsetUp, offsetDown, offsetLeft, offsetRight)
            pag.moveTo(x, y)
            return x, y


    # In[8]:


    def dragTo(self, image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=30, full_match=False):
        """Same as click func"""
        if image != None:   
            location = self.waitImageToAppear(image, imageError, timeout, full_match)     
            x, y = pag.center(location)
            x, y = self.offset(x, y, offsetUp, offsetDown, offsetLeft, offsetRight)
            pag.dragTo(x, y)
            return x, y
        else:
            x, y = self.offset(x, y, offsetUp, offsetDown, offsetLeft, offsetRight)
            pag.dragTo(x, y)
            return x, y


    # In[9]:


    def scrollUp(self, value):
        """Noticeable for values over 120"""
        pag.scroll(value)
        return value


    # In[10]:


    def scrollDown(self, value):
        """Noticeable for values over 120"""
        value = -value
        pag.scroll(value)
        return value


    # In[11]:


    def scrollLeft(self, value):
        """Noticeable for values over 120"""
        value = -int(value)
        pag.hscroll(value)
        return value


    # In[12]:


    def scrollRight(self, value):
        """Noticeable for values over 120"""
        pag.hscroll(int(value))
        return value


    # In[14]:


    def press(self, keys):
        """Press hotkeys like ctrl+c for copy and other shortcuts guddies"""
        keys = self.listifyString(keys)
        if len(keys) == 3:
            key1 = keys[0]
            key2 = keys[1]
            key3 = keys[2]
            pag.hotkey(key1, key2, key3)
            return key1, key2, key3
        elif len(keys) == 2:
            key1 = keys[0]
            key2 = keys[1]
            pag.hotkey(key1, key2)
            return key1, key2
        elif len(keys) == 1:
            key1 = keys[0]
            pag.hotkey(key1)
            return key1
        else:
            raise ValueError('Maximum 3 keys can be pressed at the same time!')


    # In[15]:


    def write(self, text, image=None, x=None, y=None, offsetUp=None, offsetDown=None, offsetLeft=None, offsetRight=None, imageError=None, timeout=30, full_match=False):
        """Type some text. Optionally in the given coordinates or image"""
        if (x == None and y == None) and (image == None):
            pag.typewrite(str(text))
            return text
        else:
            self.click(image, x, y, offsetUp, offsetDown, offsetLeft, offsetRight, imageError, timeout, full_match)
            self.press("ctrl, a")
            self.press("backspace")
            pag.typewrite(str(text))
            return text


    # In[16]:


    def waitSeconds(self, seconds):
        """Wait a few seconds.."""
        time.sleep(int(seconds))
        return seconds



    def getImageLocation(self, image, full_match=False):
        """Try to match the input image with the screenshot image. Gradually lower percentage match if image not found."""
        
        if full_match:
            location = pag.locateOnScreen(image, grayscale=False, confidence=0.99)
            return location
        else:
            location = pag.locateOnScreen(image, grayscale=False, confidence=0.99)
            
            if isinstance(location, tuple):
                return location
            elif location == None:
                location = pag.locateOnScreen(image, grayscale=True, confidence=0.95)
                if isinstance(location, tuple):
                    return location
                elif location == None:
                    location = pag.locateOnScreen(image, grayscale=True, confidence=0.90)
                    if isinstance(location, tuple):
                        return location
                    elif location == None:
                        location = pag.locateOnScreen(image, grayscale=True, confidence=0.80)
                        if isinstance(location, tuple):
                            return location
                        elif location == None:
                            location = pag.locateOnScreen(image, grayscale=True, confidence=0.70)
                            if isinstance(location, tuple):
                                return location
                        
                
    def waitColorToAppear(self, xyrgb, imageError=None, timeout=30, full_match=False):
        """Wait for RGB color to appear in the specified x,y coordinates"""
        if timeout == None:
            timeout = 1800
        else:
            try:
                timeout = int(float(timeout))
            except:
                raise ValueError("Number of seconds must be inserted not text!")
        xyrgb = self.listifyString(xyrgb)
        xyrgb = [int(n) for n in xyrgb]
        x = xyrgb[0]
        y = xyrgb[1]
        rgb = tuple(xyrgb[-3:])
        # wait rgb to appear
        wait_until = datetime.now() + timedelta(seconds=timeout)
        rgb_onscreen = False
        while rgb_onscreen == False:
            color_exists = pag.pixelMatchesColor(x, y, rgb, tolerance=50)
            if imageError != None:
                imageError = self.getImageLocation(imageError)
                if isinstance(imageError, tuple):
                    print("Image error> {}".format(str(imageError)))
                    raise ValueError("Image error found on screen!")
            elif color_exists == False:
                rgb_onscreen = False
                time.sleep(0.2)
                if wait_until < datetime.now():
                    print("RGB > {}".format(str(xyrgb)))
                    raise ValueError("Timeout reached!")
            elif color_exists == True:
                rgb_onscreen = True
                return color_exists



    def waitColorToDisappear(self, xyrgb, imageError=None, timeout=30, full_match=False):
        """Wait for RGB color to dissapear in the specified x,y coordinates"""
        if timeout == None:
            timeout = 1800
        else:
            try:
                timeout = int(float(timeout))
            except:
                raise ValueError("Number of seconds must be inserted not text!")
        xyrgb = self.listifyString(xyrgb)
        xyrgb = [int(n) for n in xyrgb]
        x = xyrgb[0]
        y = xyrgb[1]
        rgb = tuple(xyrgb[-3:])
        # wait rgb to disappear
        wait_until = datetime.now() + timedelta(seconds=timeout)
        rgb_onscreen = True
        while rgb_onscreen == True:
            color_exists = pag.pixelMatchesColor(x, y, rgb, tolerance=50)
            if imageError != None:
                imageError = self.getImageLocation(imageError)
                if isinstance(imageError, tuple):
                    print("Image error> {}".format(str(imageError)))
                    raise ValueError("Image error found on screen!")
            elif color_exists == True:
                rgb_onscreen = True
                time.sleep(0.2)
                if wait_until < datetime.now():
                    print("RGB > {}".format(str(xyrgb)))
                    raise ValueError("Timeout reached!")
            elif color_exists == False:
                rgb_onscreen = False
                return color_exists





    def waitImageToAppear(self, image, imageError=None, timeout=30, full_match=False):
        """Wait for image to appear"""
        if timeout == None:
            timeout=30
        else:
            try:
                timeout = int(float(timeout))
            except:
                raise ValueError("Number of seconds must be inserted not text!")
        wait_until = datetime.now() + timedelta(seconds=timeout)
        img_onscreen = False
        while img_onscreen == False:
            location = self.getImageLocation(image, full_match=full_match)
            if imageError != None:
                imageError = self.getImageLocation(imageError)
                if isinstance(imageError, tuple):
                    print("Image error > {}".format(str(imageError)))
                    raise ValueError("Image error found on screen!")
            elif location == None:
                img_onscreen = False
                time.sleep(0.5)
                if wait_until < datetime.now():
                    print("Image not found > {}".format(str(image)))
                    raise ValueError("Timeout reached!")
            else:
                img_onscreen = True
                return location
        


    def waitImageToDisappear(self, image, imageError=None, timeout=30, full_match=False):
        """Wait for image to disappear from the screen"""
        if timeout == None:
            timeout = 1800
        else:
            try:
                timeout = int(float(timeout))
            except:
                raise ValueError("Number of seconds must be inserted not text!")
        wait_until = datetime.now() + timedelta(seconds=timeout)
        img_onscreen = True
        while img_onscreen == True:
            location = self.getImageLocation(image, full_match=full_match)
            if imageError != None:
                imageError = self.getImageLocation(imageError)
                if isinstance(imageError, tuple):
                    print("Image error > {}".format(str(imageError)))
                    raise ValueError("Image error found on screen!")
            elif location != None:
                img_onscreen = True
                time.sleep(0.5)
                if wait_until < datetime.now():
                    print("Image didn't dissapeared > {}".format(str(image)))
                    raise ValueError("Timeout reached!")
            else:
                img_onscreen = False
                return location



    def getImageStack(self, image): 
        """Locate all images of the same type on the screen and return nested list with str xy coordinates
        Images which are the same(ex: like radio buttons) are inserted in the list 
        from UP to DOWN, and LEFT to RIGHT  
        that's the way you can count an repetead image and return it
        """
        elements = list(pag.locateAllOnScreen(image, grayscale=True, confidence=0.90))
        elementsCenter = [pag.center(elem) for elem in elements]
        elemCenterli = [list(elem) for elem in elementsCenter]

        #Cast element to str type
        elemStrli = []
        for elemli in elemCenterli:
            elemStrli.append([str(elem) for elem in elemli])
            
        return elemStrli



    def getxy(self, li):
        x = int(li[0])
        y = int(li[1])
        return x, y


    def tuplefyList(self, alist):
        newli = []
        for li in alist:
            newli.append(self.getxy(li))
        return newli


    def imageNeddle(self, image, imageNr='last'):
        """Get to coordonates for the images needed
        You can count images of the same type on the screen from UP to DOWN, and LEFT to RIGHT.
        """
        neddleli = self.getImageStack(image)
        neddleli = self.tuplefyList(neddleli)
        
        if len(neddleli) == 0:
            raise ValueError("No image found on screen!")

        if imageNr == 'first':
            neddle = neddleli[0]
            return neddle
        elif imageNr == 'last':
            neddle = neddleli[-1]
            return neddle
        elif imageNr == 'all':
            return neddleli
        else:
            neddleli = self.customFilterList(neddleli, int(float(imageNr)))
            return neddleli[0]




# Initialize class

robo = Robo()
