import pygame

def collides(s, a):
   

    return (s.posX == a.x and s.posY == a.y)
    
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
    
    # clears the screen
    gameWindow.fill((0, 0, 0));

    for i in range (len(snake)):
        snake[i].show(gameWindow)

        
    apple.show(gameWindow)

    if collides(snake_head, apple):
        tail = Snake()
        snake.append(tail)
        
        apple.update(display_width, display_height)
    pygame.display.update();

    clock.tick(15);

pygame.quit();
quit();
