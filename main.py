import pyautogui
import time


def click_accept_button():
    time.sleep(5)
    primary_width, primary_height = pyautogui.size()
    print(primary_height, primary_width)
    accept_button_location = None
    print('looking for button.')
    while accept_button_location is None:
        time.sleep(5)
        accept_button_location = pyautogui.locateOnScreen(
            'image.png', confidence=0.6, grayscale=True
        )
        print(accept_button_location)
        time.sleep(3)
    
    print("Button found !")
    accpet_button_center = pyautogui.center(accept_button_location)
    print(accpet_button_center)
    x, y = accpet_button_center
    print(x, y)
    pyautogui.moveTo(x, y, 1)
    pyautogui.click()

    print("Match accepted ! Exiting...")
    time.sleep(5)
    exit()

click_accept_button()
exit()
time.sleep(10)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("google.com")
pyautogui.hotkey("enter")