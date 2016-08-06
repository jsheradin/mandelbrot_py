#Average squares
import time

start_time = time.time()

sq_size = 6

#Get value of pixel from list
def get_pixel(x, y):
    return pixels[x + y*width]

#Load file
pixels = open("mandelbrot_big.txt", "r").read().split("\n")
pixels = pixels[:-1]
pixels = list(map(int, pixels))

width = pixels[0]
height = pixels[1]
pixels = pixels[2:]

pix_new = [int(width/sq_size), int(height/sq_size)]

#Average Blocks
for y in range(0, height, sq_size):
    for x in range(0, width, sq_size):
        block = []
        for a in range(sq_size):
            for b in range(sq_size):
                block.append(get_pixel(x+a, y+b))
        pix_new.append(int(sum(block)/sq_size**2))

with open("mandelbrot.txt", "w") as save_file:
    for pixel in pix_new:
        save_file.write("{}\n".format(pixel))
print("done in {} seconds".format(time.time() - start_time))
