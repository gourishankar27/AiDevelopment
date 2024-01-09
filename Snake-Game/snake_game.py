import pygame
import random
import sys # gives access to lots of systems functionality. 
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        # initializing with starting position of snake
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]

    def draw_snake(self):
        for block in self.body:
            # create a rectangle 
            # draw the rectangle 

            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)

            snake_rect = pygame.Rect(x_pos, y_pos, 
                                     cell_size, cell_size)
        
            pygame.draw.rect(screen, (100,20,255), snake_rect)


class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)

        print(f"FRUIT position x:{self.x} , y:{self.y}")

        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        # create a rectangle 
        # draw the rectangle 
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)

        fruit_rect = pygame.Rect(x_pos, y_pos ,
                                 cell_size, cell_size)

        pygame.draw.rect(screen,(255,30,100), fruit_rect)


#it starts the pygame 
pygame.init()

cell_size = 40
cell_number = 20
# Display surface. # set_mode((width,height))
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))

clock = pygame.time.Clock()

fruit = FRUIT()

snake = SNAKE()

while True:
    # HEre draw all the elements for game. 

    # EVENT LOOP to let the game know when to close. 
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
    
    # screen.fill(pygame.Color('yellow'))
    screen.fill((175,215,70))

    fruit.draw_fruit()
    snake.draw_snake()

    pygame.display.update()

    # To make game more consistent. 
    clock.tick(60)
