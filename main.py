from graphics import Window
from fractal import Fractal

def main():

    screen_x = 800
    screen_y = 600

    xa = -2.0
    xb = 1.0
    ya = -1.5
    yb = 2.0

    win = Window(screen_x, screen_y)
    fractal = Fractal(xa, xb, ya, yb, win)
    
    win._img.put(fractal.pixel_map_str)
    win.wait_for_close()


main()