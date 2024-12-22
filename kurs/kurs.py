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
        self.supply = True

    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);
        screen.blit(self.texture, (x, y))
    
    def resource_renewal(self):
        self.mobile = self.max_mobile
        if self.health < self.max_health:
            self.health = self.health + 1;
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
        if self.health < self.max_health:
            self.health = self.health + 1;
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
            if self.health < self.max_health:
                self.health = self.health + 1;
        else:
            self.health -= 1;
    
    

class flag:
    def __init__(self, color):
        self.texture = pygame.image.load(root_project+'flag.png');
        self.color = color;
        self.health = 20
        self.atack = 0
        self.max_health = 20
        self.max_mobile = 0
        self.mobile = 0
        self.supply = True
    def draw_element(self, screen, x, y, size):
        r = pygame.Rect(x, y, size-1, size-1);
        pygame.draw.rect(screen, self.color, r, 0);
        screen.blit(self.texture, (x, y))
    def resource_renewal(self):
        if self.health < self.max_health:
            self.health = self.health + 1;
            

class null_cell:
    def __init__(self, color):
        self.color = color;
        self.supply = True
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
        matrix[0][1] = infantry(red_team_color);
        matrix[1][0] = infantry(red_team_color);
        matrix[1][1] = infantry(red_team_color);
        matrix[-1][-1] = flag(blue_team_color);
        matrix[-1][-2] = infantry(blue_team_color);
        matrix[-2][-1] = infantry(blue_team_color);
        matrix[-2][-2] = infantry(blue_team_color);
        return matrix;
    def draw_cells(self, screen):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j].draw_element(screen, i * self.size_cell-1 + self.size_bar_x, j * self.size_cell-1, self.size_cell-1)

    def get_cell(self, coord):
        coord[0] -= self.size_bar_x;
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
    
    def movement(self, coord, coord_target, buffer_color,  bar, screen):
        field.matrix[coord_target[0]][coord_target[1]] = field.matrix[coord[0]][coord[1]]
        field.matrix[coord_target[0]][coord_target[1]].mobile -=1
        field.matrix[coord[0]][coord[1]] = null_cell(buffer_color)
        coord[0] = coord_target[0]
        coord[1] = coord_target[1]
        bar.draw_right_interface(screen, field.matrix[coord_target[0]][coord_target[1]]);
        field.draw_cells(screen)
        pygame.display.flip()

    def fire(self, coord, coord_target, buffer_color,  bar, screen):
        if ((field.matrix[coord_target[0]][coord_target[1]].health - field.matrix[coord[0]][coord[1]].atack) <= 0):
            field.matrix[coord_target[0]][coord_target[1]] = null_cell(field.matrix[coord_target[0]][coord_target[1]].color)
            field.matrix[coord[0]][coord[1]].mobile = 0
            field.draw_cells(screen)
            

        else:
            field.matrix[coord_target[0]][coord_target[1]].health -= field.matrix[coord[0]][coord[1]].atack
            field.matrix[coord[0]][coord[1]].mobile = 0
        bar.draw_right_interface(screen, field.matrix[coord[0]][coord[1]]);
        pygame.display.flip()

    def left_button_click(self, event, coord, buffer_color, bar, screen):
        coord_target = field.get_cell(list(event.pos))
        check = field.check_cell(coord_target)
        if ((check == False) and (1 == (abs(coord[0] - coord_target[0])) + (abs(coord[1] - coord_target[1]))) and (field.matrix[coord[0]][coord[1]].mobile > 0) and coord_target[0] <=19 and coord_target[0] >=0 and coord_target[1] <= 15 and coord_target[1] >= 0):
             field.movement(coord, coord_target, buffer_color, bar, screen)

        elif ((check == True) and (1 == (abs(coord[0] - coord_target[0])) + (abs(coord[1] - coord_target[1]))) and (field.matrix[coord[0]][coord[1]].mobile > 0)):
            field.fire(coord, coord_target, buffer_color, bar, screen)
        
    
    def check_selected_cell(self, event, screen, bar):
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
                              field.left_button_click(event, coord, buffer_color, bar, screen)
                        else:
                            field.matrix[coord[0]][coord[1]].color = buffer_color
                            movement = False
                            field.draw_cells(screen)
                            pygame.display.flip()
                            break
    def update(self, turn):
        for i in self.matrix:
            for j in i:
                if type(j) != flag and j.color == turn:
                    j.supply = False;
        for index in range(320):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if type(self.matrix[i][j]) != flag and self.matrix[i][j].color == turn:
                        if i < 19:
                            if (self.matrix[i+1][j].supply == True and self.matrix[i+1][j].color == turn):
                                self.matrix[i][j].supply  = True;
                        if i > 0:
                            if (self.matrix[i-1][j].supply == True and self.matrix[i-1][j].color == turn):
                                self.matrix[i][j].supply  = True;
                        if j > 0:
                            if (self.matrix[i][j-1].supply == True and self.matrix[i][j-1].color == turn):
                                self.matrix[i][j].supply  = True;
                        if j < 15:
                            if (self.matrix[i][j+1].supply == True and self.matrix[i][j+1].color == turn):
                                self.matrix[i][j].supply  = True;
    def update_units(self, turn, screen):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.check_cell([i, j]):
                    if (self.matrix[i][j].color == turn):
                        self.matrix[i][j].resource_renewal();
                        if self.matrix[i][j].health <= 0:
                            self.matrix[i][j] = null_cell(turn);
                            self.draw_cells(screen)
    def update_power(self, turn):
        power_up = 0;
        power_max = 0;
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if not self.check_cell([i, j]):
                    
                    if (self.matrix[i][j].color == turn):
                        power_max += 3;
                        power_up += 1;
        return [power_up, power_max]

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
        self.texture_infantry = pygame.image.load(root_project+'infantry.png');
        self.texture_wheel = pygame.image.load(root_project+'wheel.png');
        self.texture_tank = pygame.image.load(root_project+'tank.png');
        
        self.texture_damage = pygame.image.load(root_project+'damage.png');
        self.texture_hp = pygame.image.load(root_project+'hp.png');
        self.texture_move = pygame.image.load(root_project+'mov.png');
        self.texture_supply_true = pygame.image.load(root_project+'supply=true.png');
        self.texture_supply_false = pygame.image.load(root_project+'supply=false.png');
        
    def draw_left_interface(self, screen):
        r = pygame.Rect(0, 0, self.size_bar_x, self.size_y);
        pygame.draw.rect(screen,  black_color, r, 0);
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
        # отрисовка пехоты
        r = pygame.Rect(0, 400, 50, 50);
        pygame.draw.rect(screen, self.team , r, 0);
        screen.blit(self.texture_infantry, (0, 400))
        text = "5/tab+1";
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (60, 410))
        #отрисовка мотопехоты
        r = pygame.Rect(0, 500, 50, 50);
        pygame.draw.rect(screen, self.team , r, 0);
        screen.blit(self.texture_wheel, (0, 500))
        text = "25/tab+2";
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (60, 510))
        #отрисовка танка
        r = pygame.Rect(0, 600, 50, 50);
        pygame.draw.rect(screen, self.team , r, 0);
        screen.blit(self.texture_tank, (0, 600))
        text = "50/tab+3";
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (60, 610))
    
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
        #text = str(unit.supply);
        a = Font.render(text, 1, (100, 100, 100))
        screen.blit(a, (1260, 310))
        
        r = pygame.Rect(1200, 400, 50, 50);
        pygame.draw.rect(screen, self.team , r, 0);
        if unit.supply:
            screen.blit(self.texture_supply_true, (1201, 401))
        else:
            screen.blit(self.texture_supply_false, (1201, 401))


    def resource_renewal(self, max_power, power_up):
        self.max_power = max_power;
        self.power_up = power_up;
        self.command = self.command_max;
        self.power = self.power + self.power_up;
        if self.power > self.max_power:
            self.power = self.max_power;
        
def reverse_color(color):
    if color == blue_team_color:
        return red_team_color
    else:
        return blue_team_color
    
    
def buy_unit(event, these_selected_team):
    coord = field.get_cell(list(event.pos))
    if(field.check_cell(coord) == False and field.matrix[coord[0]][coord[1]].color == these_selected_team.team):
        field.matrix[coord[0]][coord[1]].color = black_color
        field.draw_cells(screen)
        pygame.display.flip()
        add = True
        while(add):
            for event_k in pygame.event.get():
                if event_k.type == pygame.KEYDOWN:
                    if (event_k.key == pygame.K_1 and these_selected_team.power >= 5):
                        field.matrix[coord[0]][coord[1]] = infantry(these_selected_team.team)
                        field.matrix[coord[0]][coord[1]].mobile = 0
                        these_selected_team.power -= 5
                        these_selected_team.command -= 1
                        field.draw_cells(screen)
                        these_selected_team.draw_left_interface(screen)
                        pygame.display.flip()
                        add = False

                    if (event_k.key == pygame.K_2 and these_selected_team.power >= 25):
                        field.matrix[coord[0]][coord[1]] = wheel(these_selected_team.team)
                        field.matrix[coord[0]][coord[1]].mobile = 0
                        these_selected_team.power -= 25
                        these_selected_team.command -= 1
                        field.draw_cells(screen)
                        these_selected_team.draw_left_interface(screen)
                        pygame.display.flip()
                        add = False

                    if (event_k.key == pygame.K_3 and these_selected_team.power >= 50):
                        field.matrix[coord[0]][coord[1]] = tank(these_selected_team.team)
                        field.matrix[coord[0]][coord[1]].mobile = 0
                        these_selected_team.power -= 50
                        these_selected_team.command -= 1
                        field.draw_cells(screen)
                        these_selected_team.draw_left_interface(screen)
                        pygame.display.flip()
                        add = False  

                    else:
                        field.matrix[coord[0]][coord[1]].color = these_selected_team.team
                        field.draw_cells(screen)
                        these_selected_team.draw_left_interface(screen)
                        pygame.display.flip()
                        add = False  


def new_unit(these_selected_team, field, screen):
    add_unit = True
    while(add_unit):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if (event.button == 1):
                    buy_unit(event, these_selected_team)
                else:
                    add_unit = False
                    field.draw_cells(screen)
                    these_selected_team.draw_left_interface(screen)
                    pygame.display.flip()
                    break

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
                if field.matrix[selected_element[0]][selected_element[1]].color == turn:
                    if turn == blue_team_color:
                        if (pl_bar_blue.command != 0):
                            field.check_selected_cell(event, screen, pl_bar_blue)
                            pl_bar_blue.command -= 1;
                            pl_bar_blue.draw_left_interface(screen);
                    else:
                        if (pl_bar_red.command != 0):
                            field.check_selected_cell(event, screen, pl_bar_red)
                            pl_bar_red.command -= 1;
                            pl_bar_red.draw_left_interface(screen);
                            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                field.update(turn);
                field.update_units(turn, screen);
                power_up, max_power = field.update_power(turn);
                if turn == red_team_color:
                    turn = reverse_color(turn);
                    
                    pl_bar_red.resource_renewal(max_power, power_up);
                    pl_bar_blue.draw_left_interface(screen);
                else:
                    turn = reverse_color(turn);
                    pl_bar_blue.resource_renewal(max_power, power_up);
                    pl_bar_red.draw_left_interface(screen);
            pygame.display.flip();
            if event.key == pygame.K_TAB:
                if (turn == red_team_color):
                    new_unit(pl_bar_red, field, screen)
                    pl_bar_red.draw_left_interface(screen);
                else:
                    new_unit(pl_bar_blue, field, screen)
                    pl_bar_blue.draw_left_interface(screen);
    pygame.display.flip();
