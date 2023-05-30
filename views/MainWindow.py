import tkinter as GUI

class MainWindow(GUI.Frame):
    def __init__(self, master) -> None:
        GUI.Frame.__init__(self,master)

        self.pack(fill='both')

        hello = GUI.Label(self, text="Hello",justify='center')
        hello.grid()