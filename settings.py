# COLORS (r, g, b), this was just copy paste but are the default colors for the game
import pygame
import os   
#This one is needed to simplify the process of bringing 
#the tiles from the assets, so it creates a path to the directory

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BGCOLOUR = DARKGREY

#The game settings
TILESIZE = 32 #Tiles size
ROWS = 15 #Rows
COLS = 15 #Columns
AMOUNT_MINES = 5 #Amount of mines
WIDTH = TILESIZE * ROWS #The amount of tiles * amount of rows give us the amount of pixels needed on screen
HEIGHT = TILESIZE * COLS #Same here
FPS = 60 #frames per second for the clock
TITLE = "Buscaminas" #Caption

tile_numbers = []

for i in range(1,9): 
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"Tile{i}.png")),(TILESIZE,TILESIZE)))
    #This one will create an array called tile_numbers which will basically save the tiles of numbers from 1 to 8, not 9
    #and transform.scale will just readjust our .png to 32*32 in size so every tile has the same size, and .image.load
    #will simply load the image from the directory, os.path.join is for us to be able to interact with the directory
    #so we are able to use the Tile{i} so it's easier to bring the files
    
tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileEmpty.png")),(TILESIZE,TILESIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileExploded.png")),(TILESIZE,TILESIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileFlag.png")),(TILESIZE,TILESIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileMine.png")),(TILESIZE,TILESIZE))
tile_notmine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileNotMine.png")),(TILESIZE,TILESIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileUnknown.png")),(TILESIZE,TILESIZE))
