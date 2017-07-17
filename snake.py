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

snake = Snake();
apple = Apple()

gameQuit = False;

while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True;

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.update_dir(0, -snake.rect_height);
            elif event.key == pygame.K_LEFT:
                snake.update_dir(-snake.rect_width, 0);
            elif event.key == pygame.K_RIGHT:
                snake.update_dir(snake.rect_width, 0);
            elif event.key == pygame.K_DOWN:
                snake.update_dir(0, snake.rect_height);

    snake.move();
    snake.constrain(display_width, display_height);
    
    # clears the screen
    gameWindow.fill((0, 0, 0));
    snake.show(gameWindow);
    apple.show(gameWindow)

    if collides(snake, apple):
        apple.update(display_width, display_height)
    pygame.display.update();

    clock.tick(15);

pygame.quit();
quit();
