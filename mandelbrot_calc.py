#Calculate a mandelbrot set
import pygame, time
from multiprocessing import Pool

start_time = time.time()

threads = 8

#Render space dimensions
x_min = -2
x_max = 2
y_min = -2
y_max = 2

#Resolution settings (pixels)
width = 1000
height = 1000

#Actual mandlebrot math
x_diff = (x_max - x_min)/width
y_diff = (y_max - y_min)/height
width_half = width/2
height_half = height/2
def iterate(pix):
    x = ((pix%width)-width_half)*x_diff
    y = (int(pix/height)-height_half)*y_diff
    x_temp, x_orig = x, x
    y_temp, y_orig = y, y
    loops = 0
    while (x**2 + y**2)**0.5 <= 2 and loops < 255:
        x_temp = x**2 - y**2 + x_orig
        y = 2*x*y + y_orig
        x = x_temp
        loops += 1
    return loops

if __name__ == '__main__':
    #Calculate pixel fill
    with Pool(threads) as p:
        pixels = [p.map(iterate, range(0, width*height))]
    pixels = [ent for sublist in pixels for ent in sublist]

    #Dump to file
    with open("mandelbrot.txt", "w") as save_file:
        save_file.write("{}\n{}\n".format(width, height))
        for pixel in pixels:
            save_file.write("{}\n".format(pixel))
    print("done in {} seconds".format(time.time() - start_time))
