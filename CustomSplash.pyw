import sys
import os
import winsound
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import time

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("ReiNX Custom Splash Script")

        self.pack(fill=BOTH, expand=1)

        text = Label(self, text="ReiNX Custom Splash Script", font='Helvetica 18 bold')
        text.pack()
        text1 = Label(self, text='\nSelect an image, and click "Create Splash!"')
        text1.pack()
        text2 = Label(self, text="GUI by Lunalik, Program by TheExpertNoob")
        text2.config(font=("Courier", 7))
        text2.place(x=190, y=380)
    
        button3 = Button(self, text="Select image", command=self.select_image)
        button3.place(x=155, y=80)
        button2 = Button(self, text="Close", command=self.client_exit)
        button2.place(x=200, y=350)
        self.button1 = Button(self, text="Create Splash", command=self.splash, state=DISABLED)
        self.button1.place(x=100, y=350)
        
        defaultPath = '\\resources\\blank.png'
        try:
            defaultPath = sys._MEIPASS + defaultPath
        except:
             defaultPath = os.getcwd() + defaultPath
        load = Image.open(defaultPath)
        img = load.resize((380, 214))
        render = ImageTk.PhotoImage(img)

        img = Label(self, image=render)
        img.image = render
        img.place(x=8,y=120)

    def splash(self):
        defaultPath = '\\resources\\dl.wav'
        try:
            defaultPath = sys._MEIPASS + defaultPath
            print(defaultPath)
        except:
             defaultPath = os.getcwd() + defaultPath
        winsound.PlaySound(defaultPath, winsound.SND_ASYNC)
        #Everything from here to the next comment is written by TheExpertNoob
        im = Image.open(filename, 'r')
        img = im.resize((1280, 720))
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        pixelMap = img.load()
        pixels = []
        for y in range(img.size[0]):
          for x in range(img.size[1]):
            pixels.append(pixelMap[y,x][0])
            pixels.append(pixelMap[y,x][1])
            pixels.append(pixelMap[y,x][2])
            pixels.append(0)
          for x in range(0, 48 * 4):
            pixels.append(0)
        with open('splash.bin','wb') as f:
          fileSize = 720 * 1280
          f.write(bytes(x for x in pixels))
          #Everything in between here and the previous comment is written by TheExpertNoob 

        defaultPath = '\\resources\\done.png'
        try:
            defaultPath = sys._MEIPASS + defaultPath
        except:
             defaultPath = os.getcwd() + defaultPath
        load = Image.open(defaultPath)
        img = load.resize((380, 214))
        render = ImageTk.PhotoImage(img)

        img = Label(self, image=render)
        img.image = render
        img.place(x=8,y=120)
        self.button1.config(state="disabled")



    def select_image(self):
        global file_path
        global filename
        filename = filedialog.askopenfilename(title = "Select an image")
        file_path.set(str(filename))
        if os.path.exists(filename):
            load = Image.open(filename)
            img = load.resize((380, 214))
            render = ImageTk.PhotoImage(img)

            img = Label(self, image=render)
            img.image = render
            img.place(x=8,y=120)
            self.button1.config(state="normal")


    def client_exit(self):
        sys.exit()

root = Tk()
root.geometry("400x400")
root.title("wm min/max")
root.resizable(0,0)
defaultPath = '\\resources\\splash.ico'
try:
    defaultPath = sys._MEIPASS + defaultPath
except:
    defaultPath = os.getcwd() + defaultPath
root.iconbitmap(defaultPath)
file_path = StringVar()
app = Window(root)

root.mainloop()

