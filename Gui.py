#import Pill, you need install Pillow or tkinter with -- pip install pillow -- in console
#Note: The Vscode console show you error not recognize pip, you need to used the folder and pip.exe

import tkinter
import ImagePil

class Gui:

    #Here create gui tkinter
    gui = tkinter.Tk()
    
    #Change the name in window
    gui.title("Image")

    #send parameter null and gui info, show the gui
    ImagePil.ImagePil.ImagePillow("",gui)