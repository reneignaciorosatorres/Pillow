import tkinter
import PIL
from PIL import Image 
from PIL import ImageTk

class ImagePil:
    def ImagePillow(self,gui):

        #Open the folder and image.
        imageT = PIL.Image.open('emoji/yes.png')

        #Resize image and create Antialias
        imageT = imageT.resize((25,25),Image.ANTIALIAS)

        #Create ImageTk with Pillow
        imageT = ImageTk.PhotoImage(imageT)

        #Used label with parameter image 
        imageLabel = tkinter.Label(gui, image=imageT)

        #The pack show label in windows 
        imageLabel.pack()

         #create and update gui
        gui.mainloop()