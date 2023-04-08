from graphics import Window
import math
import random

random.seed()
GG_rand = int(random.random() * 255)
BB_rand = int(random.random() * 255)

class Fractal():

    def __init__(self, xa, xb, ya, yb, win):
        self.pixel_map_str = self.mandel_pixel(xa, xb, ya, yb, win._width, win._height)
    
    def mandelbrot(self, c):
        z = complex(0, 0)
        for i in range(256):
            z = z**2 + c
            if abs(z)  > 4.:
                return i
        return 256

    def mandel_pixel(self, xa,xb,ya,yb,x,y):
        """ Returns a mandel-to-color in a string for Tk PhotoImage """

        # Color string table in PhotoImage with format #RRGGBB
        # Pick random colors pallete to display the fractal image
        clr = [ 
            "#%02x%02x%02x" % ( abs(int( math.cos((i)) * 255 )), 
                                GG_rand,
                                BB_rand,)
            for i in range(256)
        ]

        # Append the color of the centre as index 256
        clr.append(' #000000')  
   
        # Calculate mandelbrot x,y coordinates for each screen pixel

        xm = [xa + (xb - xa) * kx /x  for kx in range(x)]
        ym = [ya + (yb - ya) * ky /y  for ky in range(y)]

        # Build the PhotoImage string by calling mandel_pixel to index in the color table
        return " ".join((("{"+" ".join(clr[self.mandelbrot(complex(i,j))] for i in xm))+"}" for j in ym))
