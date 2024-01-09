import pygame
import sys # gives access to lots of systems functionality. 

#it starts the pygame 
pygame.init()

# Display surface. # set_mode((width,height))
screen = pygame.display.set_mode((600,700))

clock = pygame.time.Clock()

"""
1. Create a Surface, 
    ( import an image, write text, or create an empty space. ) 

            ORRRRRRRR

2. Display the surface ( This could be the display surface 
    or a regular surface )
"""

test_surface = pygame.Surface((50,50))
test_surface.fill((100,0,255))

x_position = 0
y_position = 0

while True:
    # HEre draw all the elements for game. 

    # EVENT LOOP to let the game know when to close. 
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
    
    # screen.fill(pygame.Color('yellow'))
    screen.fill((175,215,70))

    # x_position += 1
    # y_position += 2

    screen.blit(test_surface,(x_position,y_position))



    pygame.display.update()

    # To make game more consistent. 
    clock.tick(60)
