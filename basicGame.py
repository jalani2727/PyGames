import pygame, sys

from pygame.locals import *

#Get the program up and running 
pygame.init()

drawing_surface = pygame.display.set_mode((300, 300))

#This will draw a rectangle to the designated display. 
    #Notice that two of the arguments are tuples. Tuples are immutable lists. Use them when you know that the items that they are describing aren't going to change.
    # The third tuple contains the x position, y position and the size of the rectangle
pygame.draw.rect(drawing_surface, (0,255,0), (100,50,20,20))


pygame.display.set_caption("My First Game")


while True:
#This loop repeats forever - It continually checks whether or not the user wants th=o quit

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()