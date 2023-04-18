from tkinter import Tk, ttk

class Interface:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="Muistipeli")
        level1 = ttk.Button(master=self._root, text="Taso 1")
        level2 = ttk.Button(master=self._root, text="Taso 2")
        level3 = ttk.Button(master=self._root, text="Taso 3")

        label.pack()
        level1.pack()
        level2.pack()
        level3.pack()


window = Tk()
window.title("Muistipeli")

ui = Interface(window)
ui.start()

window.mainloop()
