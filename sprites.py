import pygame
import random
from settings import*

class Tile:
    def __init__(self, x, y, image, type, revealed = False, flagged = False): #Constructor of one single tile
        self.x= x*TILESIZE
        self.y =y *TILESIZE
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged
#we receive an x and y position to print the tile 
#the image that starts as empty tile until revealed turns true
#type which defines what type of tile is actually behind the
#revealed, and if is flagged

    def draw(self, board_surface):
        if not self.flagged and self.revealed:
            board_surface.blit(self.image, (self.x, self.y))
        elif self.flagged and not self.revealed:
            board_surface.blit(tile_flag, (self.x, self.y))
        elif not self.revealed:
            board_surface.blit(tile_unknown, (self.x, self.y))

    """def draw(self, board_surface):
        board_surface.blit(self.image,(self.x,self.y))"""

    def __repr__(self):
        return self.type
#this method __repr__ is usefull because it will work as a get and return the type of tile the object of class tile is
#And in this case will help that when we call for self.type it actually returns the type of tile
#we are working with because it's possible the .type variable saves the information of how is loaded the image
#and not the actual type we are working with, which in the case of the constructor of class Board is an ","

    


class Board:
    def __init__(self):
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        self.board_list = [[Tile(col,row,tile_empty, ",")for row in range (ROWS)]for col in range(COLS)]    
        self.mines()
        self.place_clues()
        self.digged = []

        """nested for loop to save in a list called board_list, in which in the inside [[here]] 
        in range of rows we will create "rows" amount of Tile objects in which we send the
        parameters col, row, tile_empty bc for now we don't know which kind of tile is it
        and a "," as type so it can show on console, the same for COLS :)"""

    def mines(self):
        for i in range (AMOUNT_MINES):
            while True:
                x1 = random.randint(0, ROWS-1)
                y2 = random.randint(0, COLS-1)
                if self.board_list[x1][y2].type == ",":
                    self.board_list[x1][y2].image = tile_mine #When it chooses a random x and y position we change that
                                                              #random position to a mine so we change the tile image
                    self.board_list[x1][y2].type = "M" #This is just for the console
                    break

        """So how does this work? it first will go from 0 till the amount of mines defined in settings, then it will
         loop trough them and enter an infinite loop that will choose a random x and y from 0 to 14, if what is inside
          is not already a mine, it will pute a mine, otherwise it will look another one, if it finds it, places the 
           mine, changes the image to tile_mine and changes the type to "X" for console debugging and mine verifier"""
   
    def place_clues(self):
        for x in range(ROWS): # x from 0 until rows
            for y in range(COLS): # y from 0 untils cols
                if self.board_list[x][y].type != "M": #If what is in the position x, y is diferent to a Mine continue
                    total_mines = self.look_bombs(x, y) #calls the function look_bombs to know how many bombs are around [x][y]
                    if total_mines > 0: #if there are indeed bombs around continue
                        self.board_list[x][y].image = tile_numbers[total_mines-1] # to the image tile_numbers, choose the one one with total mines-1
                        #why -1? bc the tile1.png is in the position tile_numbers[0] and so on
                        self.board_list[x][y].type = "C" # type = C for console check
            
    @staticmethod #because it doesn't receive a self parameter, so it can be called outsite the instance of board
    def inside_board( x,y):  #self is not really necessary 
        return 0<= x < ROWS and 0 <=y < ROWS #looks that the [x][y] position is still inside the board
    
    def look_bombs(self, x , y):
        total_mines = 0
        for x_off in range(-1, 2):
            for y_off in range(-1, 2): #In a bit I explain this
                neighbour_x = x + x_off
                neighbour_y = y + y_off
                if self.inside_board(neighbour_x,neighbour_y): 
                    if self.board_list[neighbour_x][neighbour_y].type == "M":
                        total_mines += 1

        return total_mines

    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface,(0,0))

    def dig(self,x , y):
        self.digged.append((x,y))
        if self.board_list[x][y].type == "M":
            self.board_list[x][y].revealed = True
            self.board_list[x][y].image = tile_exploded
            return False
        elif self.board_list[x][y].type == "C":
            self.board_list[x][y].revealed = True  
            return True
        self.board_list[x][y].revealed = True

        for row in range(max(0, x-1), min (ROWS-1, x+1)+1):
            for col in range(max(0, y-1), min (COLS-1, y+1)+1):
                if(row, col) not in self.digged:
                    self.dig(row, col)
        return True

            
        

    def displayboard(self):
        for row in self.board_list:
            print(row)