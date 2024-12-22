import pygame
from time import sleep, time
from pygame import font
import sys
#"C:/kurs/red_blue/kurs/"
#"D:/Python/red_blue/kurs/"
null_team_color = (220, 220, 220);
red_team_color = (205, 92, 92);
blue_team_color = (135, 206, 235);
black_color = (150, 150, 150);
root_project = "C:/kurs/red_blue/kurs/";

class tank:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'tank.png');
        self.color = color
        self.health = 10
        self.atack = 4
        self.max_health = 10
        self.max_mobile = 3
        self.mobile = 3

    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);
        screen.blit(self.texture, (x, y))

class infantry:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'infantry.png');
        self.color = color
        self.health = 2
        self.atack = 1
        self.max_health = 2
        self.max_mobile = 1
        self.mobile = 1

    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);
        screen.blit(self.texture, (x, y))
    
        

class wheel:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'wheel.png')
        self.color = color
        self.health = 5
        self.atack = 2
        self.max_health = 5
        self.max_mobile = 5
        self.mobile = 5

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
        matrix[-2][-2] = wheel(blue_team_color);
        matrix[-2][-1] = wheel(blue_team_color);
        return matrix;
    def draw_cells(self, screen):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j].draw_element(screen, i * self.size_cell-1 + self.size_bar_x, j * self.size_cell-1, self.size_cell-1)

    def get_cell(self, coord):
        coord[0] -= self.size_bar_x;
        print (coord[0]//self.size_cell , " " , coord[1]//self.size_cell)
        return [coord[0]//self.size_cell,coord[1]//self.size_cell];

    def check_cell(self, coord):
        print ("ebash")
        ##type(matrix[0][0]) == flag
        if (type(self.matrix[coord[0]][coord[1]]) == tank):
            return(True)

        if (type(self.matrix[coord[0]][coord[1]]) == infantry):
            return(True)

        if (type(self.matrix[coord[0]][coord[1]]) == wheel):
            print ("blyat")
            return(True)
        
        return(False)
    
    def check_selected_cell(self, event, screen):
        coord = field.get_cell(list(event.pos))
        check = field.check_cell(coord)
        if (check):
            buffer_color = field.matrix[coord[0]][coord[1]].color
            field.matrix[coord[0]][coord[1]].color = black_color
            field.draw_cells(screen)
            pygame.display.flip()
            print ("hueta")
            movement = True
            while (movement):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN: 
                        if (event.button == 1):
                            coord_target = field.get_cell(list(event.pos))
                            check = field.check_cell(coord_target)
                            if ((check == False) and (1 == (abs(coord[0] - coord_target[0])) + (abs(coord[1] - coord_target[1]))) and (field.matrix[coord[0]][coord[1]].mobile > 0)):
                                print("rot")
                                field.matrix[coord_target[0]][coord_target[1]] = field.matrix[coord[0]][coord[1]]
                                field.matrix[coord_target[0]][coord_target[1]].mobile -=1
                                field.matrix[coord[0]][coord[1]] = null_cell(buffer_color)
                                coord[0] = coord_target[0]
                                coord[1] = coord_target[1]
                                field.draw_cells(screen)
                                pygame.display.flip()
                            elif ((check == True) and (1 == (abs(coord[0] - coord_target[0])) + (abs(coord[1] - coord_target[1]))) and (field.matrix[coord[0]][coord[1]].mobile > 0)):
                                print("ANDRUHA.EBASH")
                                if ((field.matrix[coord_target[0]][coord_target[1]].health - field.matrix[coord[0]][coord[1]].atack) <= 0):
                                    field.matrix[coord_target[0]][coord_target[1]] = null_cell(field.matrix[coord_target[0]][coord_target[1]].color)
                                    field.matrix[coord[0]][coord[1]].mobile -= 1
                                    field.draw_cells(screen)
                                    pygame.display.flip()
                                else:
                                    field.matrix[coord_target[0]][coord_target[1]].health -= field.matrix[coord[0]][coord[1]].atack
                                    field.matrix[coord[0]][coord[1]].mobile -= 1       
                        else:
                            print("hue")
                            field.matrix[coord[0]][coord[1]].color = buffer_color
                            movement = False
                            field.draw_cells(screen)
                            pygame.display.flip()
                            break
class player_bar:
    def __init__(self):
        
        self.size_y = 800;
        self.position_left = 0;
        self.size_bar_x = 200;
        self.position_right = 1200;
        
        self.command_max = 10;
        self.command = 10;
        self.power = 0;
        self.max_power = 0;
        self.power_up = 0;
        
        self.texture_command = pygame.image.load(root_project+'command.png');
        self.texture_up = pygame.image.load(root_project+'up.png');
        self.texture_control = pygame.image.load(root_project+'control.png');
        
    def draw_left_interface(self, screen):
        font.init()
        Font = font.Font(None, 50)
        # отрисовка коммандного ресурса
        r = pygame.Rect(0, 100, 50, 50);
        pygame.draw.rect(screen, red_team_color, r, 0);
        screen.blit(self.texture_command, (0, 100))
        text = str(self.command) + "/" + str(self.command_max);
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (60, 110))
        
        r = pygame.Rect(0, 200, 50, 50);
        pygame.draw.rect(screen, red_team_color, r, 0);
        screen.blit(self.texture_up, (0, 200))
        text = str(self.power_up);
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (60, 210))
        
        r = pygame.Rect(0, 300, 50, 50);
        pygame.draw.rect(screen, red_team_color, r, 0);
        screen.blit(self.texture_control, (0, 300))
        text = str(self.power) + "/" + str(self.max_power);
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (60, 310))
        
pygame.init();
field = class_field();
screen = pygame.display.set_mode((field.size_x, field.size_y));
screen.fill(field.color);
field.draw_cells(screen);
wh = wheel(red_team_color);
pl = player_bar();
pl.draw_left_interface(screen);
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1: 
                selected_element = field.check_selected_cell(event, screen)
                print(selected_element)
                field.check_selected_cell(event, screen)
    pygame.display.flip();
