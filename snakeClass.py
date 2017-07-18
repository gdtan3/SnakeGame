import pygame

class Snake:

    def __init__(self):
        self.posX = 100;
        self.posY = 100;
        self.x_vel = 0;
        self.y_vel = 0;
        self.rect_width = 20;
        self.rect_height = 20;

    def update_pos(self, x, y):
        self.posX = x
        self.posY= y

    def get_pos(self):
        return [self.posX, self.posY]

    def update_dir(self, x, y):
        self.x_vel = x;
        self.y_vel = y;

    
    def move(self):
        self.posX += self.x_vel;
        self.posY += self.y_vel;


    def constrain(self, display_width, display_height):
        if self.posX <= 0:
            self.posX = 0;

        if self.posX + self.rect_width >= display_width:
            self.posX = display_width - self.rect_width;

        if self.posY <= 0:
            self.posY = 0;

        if self.posY + self.rect_height >= display_height:
            self.posY = display_height - self.rect_height;

    
    def show(self, display):
        white = (255, 255, 255);
        snake_info = [self.posX, self.posY, self.rect_width, self.rect_height];
        pygame.draw.rect(display, white, snake_info);
