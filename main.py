import tkinter as GUI
import views.MainWindow

root = GUI.Tk()
root.title("Porównanie metod całkowania numerycznego")

frame = views.MainWindow.MainWindow(root)

frame.mainloop()