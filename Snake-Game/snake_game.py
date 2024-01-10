import pygame
import random
import sys # gives access to lots of systems functionality. 
from pygame.math import Vector2


class GAME:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.score = 0

    def game_update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def check_collision(self):
        if(self.fruit.pos == self.snake.body[0]):
            """ # Now reposition the fruit """
            self.score += 1
            print(f"SCORE : {self.score}")
            self.fruit.randomize()
            """ # Add another block to the snake """
            self.snake.add_block()
            
    def check_fail(self):
        """ # check if snake is out-side of the screen. """
        # print(f"(cell_number <= self.snake.body[0].x or self.snake.body[0].x < 0) : {(cell_number <= self.snake.body[0].x or self.snake.body[0].x < 0)}")
        # print(f" self.snake.body[0].x :  {self.snake.body[0].x}")
        # print(f"(cell_number <= self.snake.body[0].y or self.snake.body[0].y < 0) : {(cell_number <= self.snake.body[0].y or self.snake.body[0].y < 0)}")
        # print(f" self.snake.body[0].y :  {self.snake.body[0].y}")

        if((cell_number <= self.snake.body[0].x or self.snake.body[0].x < 0) or 
                    (cell_number <= self.snake.body[0].y or self.snake.body[0].y < 0)) :
            self.game_over()

        """ # Check if snake hits itself """
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

        

    def game_over(self):
        pygame.quit()
        sys.exit()


class SNAKE:
    def __init__(self):
        # initializing with starting position of snake
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False 
        # Default value for new_block will be false, 
        # and whenever snake eats fruit, it will be True

    def draw_snake(self):
        for block in self.body:
            """ # create a rectangle """

            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)

            snake_rect = pygame.Rect(x_pos, y_pos, 
                                     cell_size, cell_size)
        
            """ # draw the rectangle """
            pygame.draw.rect(screen, (100,20,255), snake_rect)

    def move_snake(self):
        """     ## MOVING THE SNAKE ## 
            1. Head is moved to a new block
            2. The block before the head gets the position where 
            the head used to be. 
            3. Each block is moved to the position of the block 
            that used to be before it.
            4. deletes the last block.   
        """
        if(self.new_block):
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            # after adding new block, setting new_block to False
            # until snake eats next fruit. 
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
        

    def add_block(self):
        self.new_block = True



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

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)

        print(f"NEW FRUIT position x:{self.x} , y:{self.y}")

        self.pos = Vector2(self.x, self.y)


#it starts the pygame 
pygame.init()

cell_size = 40
cell_number = 20
# Display surface. # set_mode((width,height))
screen = pygame.display.set_mode((cell_number*cell_size, 
                                    cell_number*cell_size))

clock = pygame.time.Clock()

# fruit = FRUIT()
# snake = SNAKE()

main_game = GAME()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    # HEre draw all the elements for game. 

    # EVENT LOOP to let the game know when to close. 
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

        if(event.type == SCREEN_UPDATE):
            # snake.move_snake()
            main_game.game_update()

        if(event.type == pygame.KEYDOWN):

            if(event.key == pygame.K_UP):
                # if(not main_game.snake.direction == Vector2(0,1)):
                if(main_game.snake.direction.y != 1):
                    main_game.snake.direction = Vector2(0,-1)

            elif(event.key == pygame.K_DOWN):
                if(main_game.snake.direction.y != -1):
                    main_game.snake.direction = Vector2(0,1)

            elif(event.key == pygame.K_LEFT):
                if(main_game.snake.direction.x != 1):
                    main_game.snake.direction = Vector2(-1,0)
            
            elif(event.key == pygame.K_RIGHT):
                if(main_game.snake.direction.x != -1):
                    main_game.snake.direction = Vector2(1,0)
    
    # screen.fill(pygame.Color('yellow'))
    screen.fill((175,215,70))

    # fruit.draw_fruit()
    # snake.draw_snake()
    main_game.draw_elements()

    

    pygame.display.update()

    # To make game more consistent. 
    clock.tick(60)
