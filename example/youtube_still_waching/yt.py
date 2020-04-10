from pyrobogui import robo, pag


def i_am_waching():
    print("Waiting for 'Are you still waching!' dialog..")
    robo.waitImageToAppear(image="still_waching.jpg", timeout=10000)
    robo.click(image="yes_still_waching.jpg")
    print("Yep, I'm waching I'm still in quarantine!")
    i_am_waching()


#Running the func
i_am_waching()





