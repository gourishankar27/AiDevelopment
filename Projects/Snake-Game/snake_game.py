import pygame
import random
import sys # gives access to lots of systems functionality. 
from pygame.math import Vector2
from enum import Enum


class GAME:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.score = 0
        self.level = 1

    def game_update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.update_level()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()

    def check_collision(self):
        if(self.fruit.pos == self.snake.body[0]):
            """ # Now reposition the fruit """
            self.fruit.randomize()
            """ # Add another block to the snake """
            self.snake.add_block()

            self.score +=1


        """ If fruit is on the skanes body, randomize it again"""
        for block in self.snake.body[:]:
            if(block == self.fruit.pos):
                self.fruit.randomize()
            
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
        # print( f"  self.snake.body : { self.snake.body}")
        for block in self.snake.body[1:]:
            # print(f" block : {block}")
            # print(f" self.snake.body[0] : {self.snake.body[0]}")
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self):
        score_text = f"Score: {self.score} Level: {self.level}"
        score_surface = game_font.render(score_text, True, (56,74,12))
        
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)
    
    def update_level(self):
        LEVEL_1 = 300
        LEVEL_2 = 200
        LEVEL_3 = 125
        LEVEL_4 = 80
        LEVEL_5 = 50

        game_level = LEVEL_1
        if(self.score >= 75):
            game_level = LEVEL_5
            self.level = 5
        elif(self.score >= 40):
            game_level = LEVEL_4
            self.level = 4
        elif(self.score >= 20):
            game_level = LEVEL_3
            self.level = 3
        elif(self.score >= 5):
            game_level = LEVEL_2
            self.level = 2

        print(f" CURRET SCORE : {self.score} :: LEVEL : {game_level}")
        pygame.time.set_timer(SCREEN_UPDATE, int(game_level))
        

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
            pygame.draw.rect(screen, (200,20,200), snake_rect)

            pygame.draw.rect(screen, (100,20,255), pygame.Rect(x_pos+4,y_pos+4,14,14))

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
            # print(f" self.direction : {self.direction}")
            # print(f" BEFORE body : {self.body}")

            if(self.direction.x != 0 or self.direction.y != 0):    
                body_copy = self.body[:-1]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]
            
            # print(f" AFTER body : {self.body}")
        

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

        # pygame.draw.rect(screen,(255,30,100), fruit_rect)
        #insted of rectangle now we will draw apple. 

        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)

        print(f"NEW FRUIT position x:{self.x} , y:{self.y}")

        self.pos = Vector2(self.x, self.y)


#it starts the pygame 
pygame.init()

cell_size = 20
cell_number = 20
SNAKE_SPEED = 300 # LOWER is FASTER
width = cell_number*cell_size
height = cell_number*cell_size
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

apple = pygame.image.load('img/apple.png')
apple = pygame.transform.scale(apple,(cell_size,cell_size))

game_font = pygame.font.SysFont('arial', 15)

main_game = GAME()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, SNAKE_SPEED)

while True:
    # HEre draw all the elements for game. 

    # EVENT LOOP to let the game know when to close. 
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

        if(event.type == SCREEN_UPDATE):
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
    
    screen.fill((175,215,70))

    main_game.draw_elements()

    pygame.display.update()

    # To make game more consistent. 
    clock.tick(60)
