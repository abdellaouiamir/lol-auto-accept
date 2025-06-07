import pyautogui
import time


def click_button(buttonImage, confidence=0.6, grayscale=True):
    print('looking for button.')
    test = False
    while not test:
        try:
            button_location = pyautogui.locateOnScreen(
                buttonImage, confidence=confidence, grayscale=grayscale
            )
            test = True
        except Exception as e:
            pass
        time.sleep(2)
    print("Button found !")
    x, y = pyautogui.center(button_location)
    pyautogui.moveTo(x, y, 1)
    pyautogui.click()
def enter_text(boxImage, text):
    click_button(boxImage)
    pyautogui.typewrite(text)

#click_button("./imageParty.png")
#enter_text("./imageSearch.png", "gwen")
def accept_gwen():
    click_button("./imageAccept.png")
    enter_text("./imageAcceptSearch.png", "gwen")
    click_button("./imageGwen.png", grayscale=False)
    click_button("./imageLockIn.png", confidence=0.8)
accept_gwen()
exit()
primary_width, primary_height = pyautogui.size()
pyautogui.hotkey('g', 'w', 'e', 'n', 'enter')
print(primary_height, primary_width)
time.sleep(10)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("google.com")
pyautogui.hotkey("enter")