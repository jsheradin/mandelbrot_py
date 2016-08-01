#Draw mandelbrot set
import pygame, sys, random

#Load file
pixels = open("mandelbrot.txt", "r").read().split("\n")
pixels = pixels[:-1]
pixels = list(map(int, pixels))

width = pixels[0]
height = pixels[1]
pixels = pixels[2:]


#Draw list
screen = pygame.display.set_mode((width, height))
pixel = pygame.Surface((1, 1))

for w in range (height):
    for h in range (width):
        pixel.fill(pixels[w+(h*width)])
        screen.blit(pixel, pygame.Rect(w+1, h+1, 1, 1))
pygame.display.flip()
pygame.image.save(screen, "mandelbrot {}x{}.png".format(width, height))
