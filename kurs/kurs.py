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
root_project = "D:/Python/red_blue/kurs/";

class tank:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'tank.png');
        self.color = color
        self.health = 10
        self.atack = 4
        self.max_health = 10
        self.max_mobile = 3
        self.mobile = 3
        self.supply = True

    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);
        screen.blit(self.texture, (x, y))
    
    def resource_renewal(self):
        self.mobile = self.max_mobile
        if self.supply:
            self.health = (self.health + 1) % self.max_health;
        else:
            self.health -= 1;

class infantry:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'infantry.png');
        self.color = color
        self.health = 2
        self.atack = 1
        self.max_health = 2
        self.max_mobile = 1
        self.mobile = 1
        self.supply = True

    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);
        screen.blit(self.texture, (x, y))
        
    def resource_renewal(self):
        self.mobile = self.max_mobile
        if self.supply:
            self.health = (self.health + 1) % self.max_health;
        else:
            self.health -= 1;
        

class wheel:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'wheel.png')
        self.color = color
        self.health = 5
        self.atack = 2
        self.max_health = 5
        self.max_mobile = 5
        self.mobile = 5
        self.supply = True

    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);
        screen.blit(self.texture, (x, y))
        
    def resource_renewal(self):
        self.mobile = self.max_mobile
        if self.supply:
            self.health = (self.health + 1) % self.max_health;
        else:
            self.health -= 1;
    
    

class flag:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'flag.png');
        self.color = color;
        self.health = 20
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
        matrix[-2][-2] = tank(blue_team_color);
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
        ##type(matrix[0][0]) == flag
        if coord[0] <=19 and coord[0] >=0 and coord[1] <= 15 and coord[1] >= 0:

            if (type(self.matrix[coord[0]][coord[1]]) == tank):
                return(True)

            if (type(self.matrix[coord[0]][coord[1]]) == infantry):
                return(True)

            if (type(self.matrix[coord[0]][coord[1]]) == wheel):
                return(True)
            
            if (type(self.matrix[coord[0]][coord[1]]) == flag):
                return(True)
            
        return(False)
    
    def movement(self, coord, coord_target, buffer_color):
        field.matrix[coord_target[0]][coord_target[1]] = field.matrix[coord[0]][coord[1]]
        field.matrix[coord_target[0]][coord_target[1]].mobile -=1
        field.matrix[coord[0]][coord[1]] = null_cell(buffer_color)
        coord[0] = coord_target[0]
        coord[1] = coord_target[1]
        field.draw_cells(screen)
        pygame.display.flip()

    def fire(self, coord, coord_target, buffer_color):
        if ((field.matrix[coord_target[0]][coord_target[1]].health - field.matrix[coord[0]][coord[1]].atack) <= 0):
            field.matrix[coord_target[0]][coord_target[1]] = null_cell(field.matrix[coord_target[0]][coord_target[1]].color)
            field.matrix[coord[0]][coord[1]].mobile = 0
            field.draw_cells(screen)
            pygame.display.flip()

        else:
            field.matrix[coord_target[0]][coord_target[1]].health -= field.matrix[coord[0]][coord[1]].atack
            field.matrix[coord[0]][coord[1]].mobile = 0

    def left_button_click(self, event, coord, buffer_color):
        coord_target = field.get_cell(list(event.pos))
        check = field.check_cell(coord_target)
        if ((check == False) and (1 == (abs(coord[0] - coord_target[0])) + (abs(coord[1] - coord_target[1]))) and (field.matrix[coord[0]][coord[1]].mobile > 0) and coord_target[0] <=19 and coord_target[0] >=0 and coord_target[1] <= 15 and coord_target[1] >= 0):
             field.movement(coord, coord_target, buffer_color)

        elif ((check == True) and (1 == (abs(coord[0] - coord_target[0])) + (abs(coord[1] - coord_target[1]))) and (field.matrix[coord[0]][coord[1]].mobile > 0)):
            field.fire(coord, coord_target, buffer_color)
        
    
    def check_selected_cell(self, event, screen):
        coord = field.get_cell(list(event.pos))
        check = field.check_cell(coord)
        if (check):
            buffer_color = field.matrix[coord[0]][coord[1]].color
            field.matrix[coord[0]][coord[1]].color = black_color
            field.draw_cells(screen)
            pygame.display.flip()
            movement = True
            while (movement):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN: 
                        if (event.button == 1):
                              field.left_button_click(event, coord, buffer_color)
                        else:
                            print("hue")
                            field.matrix[coord[0]][coord[1]].color = buffer_color
                            movement = False
                            field.draw_cells(screen)
                            pygame.display.flip()
                            break

class player_bar:
    def __init__(self, color):
        self.team = color;
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
        
        self.texture_damage = pygame.image.load(root_project+'damage.png');
        self.texture_hp = pygame.image.load(root_project+'hp.png');
        self.texture_move = pygame.image.load(root_project+'mov.png');
        
    def draw_left_interface(self, screen):
        font.init()
        Font = font.Font(None, 50)
        # отрисовка коммандного ресурса
        r = pygame.Rect(0, 100, 50, 50);
        pygame.draw.rect(screen, self.team , r, 0);
        screen.blit(self.texture_command, (0, 100))
        text = str(self.command) + "/" + str(self.command_max);
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (60, 110))
        #отрисовка прироста влияние
        r = pygame.Rect(0, 200, 50, 50);
        pygame.draw.rect(screen, self.team , r, 0);
        screen.blit(self.texture_up, (0, 200))
        text = str(self.power_up);
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (60, 210))
        #отрисовка влияния
        r = pygame.Rect(0, 300, 50, 50);
        pygame.draw.rect(screen, self.team , r, 0);
        screen.blit(self.texture_control, (0, 300))
        text = str(self.power) + "/" + str(self.max_power);
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (60, 310))
    
    def draw_right_interface(self, screen, unit):
        r = pygame.Rect(1200, 0, self.size_bar_x, self.size_y);
        pygame.draw.rect(screen,  black_color, r, 0);
        font.init()
        Font = font.Font(None, 50)
        #отрисовка урона
        r = pygame.Rect(1200, 100, 50, 50);
        pygame.draw.rect(screen, self.team , r, 0);
        screen.blit(self.texture_damage, (1200, 100))
        text = str(unit.atack);
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (1260, 110))
        #отрисовка здоровья
        r = pygame.Rect(1200, 200, 50, 50);
        pygame.draw.rect(screen, self.team , r, 0);
        screen.blit(self.texture_hp, (1201, 201))
        text = str(unit.health) + "/" + str(unit.max_health);
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (1260, 210))
        #отрисовка движения
        r = pygame.Rect(1200, 300, 50, 50);
        pygame.draw.rect(screen, self.team , r, 0);
        screen.blit(self.texture_move, (1201, 301))
        text = str(unit.mobile) + "/" + str(unit.max_mobile);
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (1260, 310))


    def resource_renewal(self):
        self.command = self.command_max;
        self.power = (self.power + self.power_up) % self.command_max;
        
def reverse_color(color):
    if color == blue_team_color:
        return red_team_color
    else:
        return blue_team_color

pygame.init();
field = class_field();
screen = pygame.display.set_mode((field.size_x, field.size_y));
screen.fill(field.color);
field.draw_cells(screen);

pl_bar_red = player_bar(red_team_color);
pl_bar_blue = player_bar(blue_team_color);
turn = red_team_color;
pl_bar_red.draw_left_interface(screen);
wh = wheel(red_team_color);
pl_bar_red.draw_right_interface(screen, wh);
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1: 
                selected_element = field.get_cell(list(event.pos))
                if (field.check_cell(selected_element)):
                    pl_bar_red.draw_right_interface(screen, field.matrix[selected_element[0]][selected_element[1]]);
                field.check_selected_cell(event, screen)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if turn == red_team_color:
                    turn = reverse_color(turn);
                    print("a");
                    pl_bar_blue.draw_left_interface(screen);
                else:
                    turn = reverse_color(turn);
                    pl_bar_red.draw_left_interface(screen);
    pygame.display.flip();
