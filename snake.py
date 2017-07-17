import pygame

pygame.init();

display_width = 800;
display_height = 600;
gameWindow = pygame.display.set_mode((display_width, display_height));

clock = pygame.time.Clock();

from snakeClass import Snake;
snake = Snake();

gameQuit = False;

while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True;

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.update_dir(0, -10);
            elif event.key == pygame.K_LEFT:
                snake.update_dir(-10, 0);
            elif event.key == pygame.K_RIGHT:
                snake.update_dir(10, 0);
            elif event.key == pygame.K_DOWN:
                snake.update_dir(0, 10);

    snake.move();
    snake.constrain(display_width, display_height);
    
    # clears the screen
    gameWindow.fill((0, 0, 0));
    snake.show(gameWindow);
    pygame.display.update();

    clock.tick(30);

pygame.quit();
quit();
