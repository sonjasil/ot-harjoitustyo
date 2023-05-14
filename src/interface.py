from tkinter import Tk, ttk, Button
from src.run_game import MatchingGame


class Interface:
    """ Luokka, joka luo graafisen käyttöliittymän muistipelin tason valinnalle."""

    def __init__(self, root):
        self._root = root

    def start(self):
        """ Luo tasonvalinnan näkymän, jossa painikkeet, jotka käynnistävät pelin eri tasot.

        """

        label = ttk.Label(master=self._root,
                          text="Muistipeli", font=("Arial", 25))
        command1 = self._start_level1
        command2 = self._start_level2
        command3 = self._start_level3
        level1 = Button(master=self._root, text="Taso 1",
                        height=5, width=10, command=command1)
        level2 = Button(master=self._root, text="Taso 2",
                        height=5, width=10, command=command2)
        level3 = Button(master=self._root, text="Taso 3",
                        height=5, width=10, command=command3)

        label.grid(row=0, column=0)
        label.grid_rowconfigure(1, weight=1)
        label.grid_columnconfigure(0, weight=1)

        level1.grid(row=1, column=0)
        level2.grid(row=2, column=0)
        level3.grid(row=3, column=0)

    def _start_level1(self):
        """ Käynnistää pelin tason 1.

        """

        game = MatchingGame(1)
        game.run_game()

    def _start_level2(self):
        """ Käynnistää pelin tason 2.

        """

        game = MatchingGame(2)
        game.run_game()

    def _start_level3(self):
        """ Käynnistää pelin tason 3.
        """

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
