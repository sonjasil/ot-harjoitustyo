from tkinter import Tk, ttk, Button
from run_game import MatchingGame

class Interface:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="Muistipeli", font=("Arial", 25))
        command1 = self._start_level1
        command2 = self._start_level2
        command3 = self._start_level3
        level1 = Button(master=self._root, text="Taso 1", height=5, width=10, command=command1)
        level2 = Button(master=self._root, text="Taso 2", height=5, width=10, command=command2)
        level3 = Button(master=self._root, text="Taso 3", height=5, width=10, command=command3)

        label.grid(row=0, column=0)
        label.grid_rowconfigure(1, weight=1)
        label.grid_columnconfigure(0, weight=1)

        level1.grid(row=1, column=0)
        level2.grid(row=2, column=0)
        level3.grid(row=3, column=0)

    def _start_level1(self):
        game = MatchingGame(1)
        game.run_game()

    def _start_level2(self):
        game = MatchingGame(2)
        game.run_game()

    def _start_level3(self):
        game = MatchingGame(3)
        game.run_game()



window = Tk()
window.geometry("700x700")
window.resizable(False, False)
window.title("Muistipeli")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

ui = Interface(window)
ui.start()

window.mainloop()
