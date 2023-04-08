from graphics import Window

class Fractal():

    def __init__(self, xa, xb, ya, yb, win):
        self.pixel_map = self.mandelbrot(xa, xb, ya, yb, win._width, win._height)
    
    def mandel_pixel(self, c):
        maxIt = 256
        z =  c   
        for i in range(maxIt):
            a = z * z
            z=a + c
            if a.real  >= 4.:
                return i
        return 256

    def mandelbrot(self, xa,xb,ya,yb,x,y):
        """ returns a mandelbrot in a string for Tk PhotoImage"""
        #color string table in Photoimage format #RRGGBB 
        clr=[ ' #%02x%02x%02x' % (int(255*((i/255)**.25)),0,0) for i in range(256)]
        clr.append(' #000000')  #append the color of the centre as index 256
        #calculate mandelbrot x,y coordinates for each screen pixel
        xm=[xa + (xb - xa) * kx /x  for kx in range(x)]
        ym=[ya + (yb - ya) * ky /y  for ky in range(y)]
        #build the Photoimage string by calling mandel_pixel to index in the color table
        return" ".join((("{"+" ".join(clr[self.mandel_pixel(complex(i,j))] for i in xm))+"}" for j in ym))
