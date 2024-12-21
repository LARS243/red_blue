import pygame
from pygame.color import THECOLORS
import sys
#"C:/kurs/red_blue/kurs/"
#"D:/Python/red_blue/kurs"
null_team_color = (220, 220, 220);
red_team_color = (205, 92, 92);
blue_team_color = (135, 206, 235);
black_color = (150, 150, 150);
root_project = "D:/Python/red_blue/kurs/";

class tank:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'tank.png');
        self.color = color
        health = 10
        atack = 4
        max_health = 10
        max_mobile = 3

    def get_health(self):
        return (self.health)

    def get_max_mobile(self):
        return(self.max_mobile)

    def get_atack(self):
        return(self.atack)

    def set_health(self, new_health):
        self.health = new_health

    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);
        screen.blit(self.texture, (x, y))

class infantry:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'infantry.png');
        self.color = color
        health = 2
        atack = 1
        max_health = 2
        max_mobile = 1

    def get_health(self):
        return (self.health)

    def get_max_mobile(self):
        return(self.max_mobile)

    def get_atack(self):
        return(self.atack)

    def set_health(self, new_health):
        self.health = new_health

    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);
        screen.blit(self.texture, (x, y))
    
        

class wheel:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'wheel.png')
        self.color = color
        health = 5
        atack = 2
        max_health = 5
        max_mobile = 5

    def get_health(self):
        return (self.health)

    def get_max_mobile(self):
        return(self.max_mobile)

    def get_atack(self):
        return(self.atack)

    def set_health(self, new_health):
        self.health = new_health

    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);
        screen.blit(self.texture, (x, y))
    
    
    

class flag:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'flag.png');
        self.color = color;
    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);
        screen.blit(self.texture, (x, y))

class null_cell:
    def __init__(self, color):
        self.color = color;
    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);

class class_field:
    def __init__(self):
        self.size_x = 1400;
        self.size_y = 800;
        self.size_bar_x = 200;
        self.size_cell = 50;
        self.color = black_color;
        self.matrix = self.create_matrix();
    def create_matrix(self):
        matrix = list();
        for i in range((self.size_x-self.size_bar_x*2) // self.size_cell):
            spisok = list();
            for j in range(self.size_y // self.size_cell):
                spisok.append(null_cell(null_team_color));
            matrix.append(spisok);
        matrix[0][0] = flag(red_team_color);
        matrix[0][1].color = red_team_color;
        matrix[1][0].color = red_team_color;
        matrix[1][1].color = red_team_color;
        
        matrix[-1][-1] = flag(blue_team_color);
        matrix[-1][-2].color = blue_team_color;
        matrix[-2][-1].color = blue_team_color;
        matrix[-2][-2].color = blue_team_color;
        return matrix;
    def draw_cells(self, screen):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j].draw_element(screen, i * self.size_cell-1 + self.size_bar_x, j * self.size_cell-1, self.size_cell-1)
                


pygame.init();
field = class_field();
screen = pygame.display.set_mode((field.size_x, field.size_y));
screen.fill(field.color);
field.draw_cells(screen);
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip();
