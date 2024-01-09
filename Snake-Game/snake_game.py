import pygame
import sys # gives access to lots of systems functionality. 

#it starts the pygame 
pygame.init()

# Display surface. # set_mode((width,height))
screen = pygame.display.set_mode((600,700))

clock = pygame.time.Clock()

"""
Display the surface 
( This could be the display surface or a regular surface )
"""

test_surface = pygame.Surface((250,250))
test_surface.fill((100,0,255))


# test_rect = pygame.Rect(100,200,100,100)

# test_rect = test_surface.get_rect( center = (400,250) )
test_rect = test_surface.get_rect( topright = (400,250) )

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

    test_rect.right += 1 

    # pygame.draw.rect(screen,(255,0,50), test_rect)
    # pygame.draw.ellipse(screen,(255,0,50), test_rect)

    screen.blit(test_surface,test_rect)



    pygame.display.update()

    # To make game more consistent. 
    clock.tick(60)
