import tkinter as tk
# import pyautogui

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def testMethod(self):
        print("this was a test")

    # def guiTest(self):
    #     screenWidth, screenHeight = pyautogui.size()
    #     currentMouseX, currentMouseY = pyautogui.position()
    #     pyautogui.moveTo(100, 150)

root = tk.Tk()
app = Application(master=root)
app.mainloop()