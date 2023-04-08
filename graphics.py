from tkinter import Tk, Canvas, PhotoImage, NW


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self._width = width
        self._height = height
        self.__canvas = Canvas(self.__root, width = width, height = height, bg = "#000000")
        self.__canvas.pack()
        self._img = PhotoImage(width = width, height = height)
        self.__canvas.create_image((0, 0), image = self._img, state = "normal", anchor = NW)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False
