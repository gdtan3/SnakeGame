import pygame
import time

def collides(s, a):
   

    return (s.posX == a.x and s.posY == a.y)

def self_collision(snake):
    sh = snake[0]
    sh_x, sh_y = sh.get_pos()
    for i in range (1, len(snake)):
        cur_x, cur_y = snake[i].get_pos()
        if sh_x == cur_x and sh_y == cur_y:
            return True

    return False

def collides_wall(sh, display_width, display_height):
    sh_x, sh_y = sh.get_pos()

    if sh_x <= 0 or (sh_x+ sh.rect_width) >= display_width:
        return True
    if sh_y <= 0 or (sh_y + sh.rect_height) >= display_height:
        return True
    return False
        
    
pygame.init();

display_width = 800;
display_height = 600;
gameWindow = pygame.display.set_mode((display_width, display_height));

clock = pygame.time.Clock();

from snakeClass import Snake;
from appleClass import Apple;

snake = []
snake_head = Snake();
apple = Apple()
snake.append(snake_head)

gameQuit = False;

while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True;

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_head.update_dir(0, -snake_head.rect_height);
            elif event.key == pygame.K_LEFT:
                snake_head.update_dir(-snake_head.rect_width, 0);
            elif event.key == pygame.K_RIGHT:
                snake_head.update_dir(snake_head.rect_width, 0);
            elif event.key == pygame.K_DOWN:
                snake_head.update_dir(0, snake_head.rect_height);

    for i in range (len(snake)-1, 0, -1):
        snaketail = snake[i]
        snaketail.update_pos(snake[i-1].posX, snake[i-1].posY)
        

    snake_head.move();    
    snake_head.constrain(display_width, display_height);

    if self_collision(snake):
        gameWindow.fill((255,0,0))
        pygame.display.update();
        time.sleep(3)
        gameQuit = True

    if collides_wall(snake[0], display_width, display_height):
        gameWindow.fill((255,0,0))
        pygame.display.update();
        time.sleep(3)
        gameQuit = True

    
    # clears the screen
    gameWindow.fill((0, 0, 0));

    for i in range (len(snake)):
        snake[i].show(gameWindow)

        
    apple.show(gameWindow)

    if collides(snake_head, apple):
        tail = Snake()
        snake.append(tail)
        
        apple.update(display_width, display_height)
        q = 0
        #checks whether Apple's location is in the snake
        while True:
            for j in range (len(snake)):
                snake_x, snake_y = snake[j].get_pos()
                apple_x, apple_y = apple.get_pos()
                if apple_x == snake_x and apple_y == snake_y:
                    apple.update(display_width, display_height)
                    q = 0
                    break
                else:
                    q = 1
                    

            if q == 1:
                break
    pygame.display.update();

    clock.tick(15);

pygame.quit();
quit();
