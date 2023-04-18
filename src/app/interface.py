from tkinter import Tk, ttk, constants
from draw_grid import main

class Interface:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="Muistipeli", font=("Arial", 25))
        level1 = ttk.Button(master=self._root, text="Taso 1", command=self._start_level1)
        level2 = ttk.Button(master=self._root, text="Taso 2", command=self._start_level2)
        level3 = ttk.Button(master=self._root, text="Taso 3", command=self._start_level_3)

        label.grid(row=0, column=0)
        label.grid_rowconfigure(1, weight=1)
        label.grid_columnconfigure(0, weight=1)

        level1.grid(row=1, column=0)
        level2.grid(row=2, column=0)
        level3.grid(row=3, column=0)

    def _start_level1(self):
        main(1)

    def _start_level2(self):
        main(2)

    def _start_level_3(self):
        main(3)



window = Tk()
window.geometry("700x700")
window.resizable(False, False)
window.title("Muistipeli")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

ui = Interface(window)
ui.start()

window.mainloop()
