import pyautogui
from PIL import Image,ImageGrab
import time
time.sleep(1)
def play(data):
    for i in range(500,536):
        for j in range(223,257):
            if data[i,j]<100:
                pyautogui.keyDown('up')

                return
    for i in range(450 , 505):
        for j in range(180 , 223):
            if data[i,j]<100:
                pyautogui.keyDown('down')
                time.sleep(0.15)
                pyautogui.keyUp('down')
                return



    return






def draw():

    frame = ImageGrab.grab().convert('L');

    for i in range(450,505):
        for j in range(180,223):
            data=frame.load()
            data[i,j]=70
    for i in range(480,535):
        for j in range(223,257):
            data=frame.load()
            data[i,j]=0
    frame.show()


if __name__=='__main__':

      #draw()
      pyautogui.press('up')
      while True:

         frame = ImageGrab.grab().convert('L')
         data = frame.load()
         play(data)




