import tkinter as GUI
from tkinter.ttk import Treeview

class MainWindow:
    def __init__(self):
        self.root = GUI.Tk()
        self.root.title("Porównanie metod całkowania numerycznego")

        self.root.grid()

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(5, weight=1)

        self.formula_l = GUI.Label(self.root, text="Formuła do obliczenia:", justify='left')
        self.formula_l.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        self.formula_w = GUI.Entry(self.root)
        self.formula_w.grid(row=0, column=1, sticky='we', padx=5, pady=5)

        self.min_x_l = GUI.Label(self.root, text="Początek całki ozn. z X:")
        self.min_x_l.grid(row=1, column=0, sticky='w', padx=5, pady=5)

        self.min_x_w = GUI.Spinbox(self.root, values=0.0, from_=-100000.0, to=100000.0, increment=0.5)
        self.min_x_w.grid(row=1, column=1, sticky='we', padx=5, pady=5)

        self.max_x_l = GUI.Label(self.root, text="Koniec całki ozn. z X:")
        self.max_x_l.grid(row=2, column=0, sticky='w', padx=5, pady=5)

        self.max_x_w = GUI.Spinbox(self.root, values=0.0, from_=-100000.0, to=100000.0, increment=0.5)
        self.max_x_w.grid(row=2, column=1, sticky='we', padx=5, pady=5)

        self.dx_l = GUI.Label(self.root, text="Wielkość skoku całki (dx):")
        self.dx_l.grid(row=3, column=0, sticky='w', padx=5, pady=5)

        self.dx_w = GUI.Spinbox(self.root, values=0.0001, from_=0.0001, to=100.0, increment=0.1)
        self.dx_w.grid(row=3, column=1, sticky='we', padx=5, pady=5)

        self.btn = GUI.Button(self.root, text="Oblicz")
        self.btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.points_list_l = GUI.Label(self.root, text="Tabela wynikowa:")
        self.points_list_l.grid(row=5, column=0, sticky='w', padx=5, pady=5)

        self.points_list_w = Treeview(self.root)
        self.points_list_w.grid(row=5, column=1, sticky='wesn', padx=5, pady=5)
        self.points_list_w['columns'] = ["x", "y1", "y2", "y3"]

        self.points_list_w.column("#0", width=0, stretch=GUI.NO)
        self.points_list_w.heading("x", text="x")
        self.points_list_w.heading("y1", text="Metoda prostokątów")
        self.points_list_w.heading("y2", text="Metoda trapezów")
        self.points_list_w.heading("y3", text="Metoda parabol")

    def show(self):
        self.root.mainloop()