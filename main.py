import pygame
from settings import *
from sprites import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def new(self): #creates a new game
        self.board = Board()
        self.board.displayboard()

    def run(self): #Runs the clock and methods of the loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
        else:
            self.end_screen()

    def draw(self): #Fills the windows with BGCOLOUR
        self.screen.fill(BGCOLOUR) #Sets the whole screen with BGCOLOUR from settings
        self.board.draw(self.screen) #Calls the method draw from Board class of object board
        pygame.display.flip() #Let pygame refresh a certain area of the screen 

    def check_win(self):
        for row in self.board.board_list:
            for tile in row:
                if tile.type != "M" and not tile.revealed:
                    return False
        return True

    def events(self): #Just to keep the game playing until the user closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx //= TILESIZE
                my //= TILESIZE

                if event.button == 1:
                    if not self.board.board_list[mx][my].flagged:
                        if not self.board.dig(mx,my):

                            for row in self.board.board_list:
                                for tile in row:
                                    if tile.flagged and tile.type != "M":
                                        tile.flagged = False
                                        tile.revealed = True
                                        tile.image = tile_notmine
                                    elif tile.type == "M":
                                        tile.revealed
                            self.playing = False    

                if event.button == 3:
                    if not self.board.board_list[mx][my].revealed:
                        self.board.board_list[mx][my].flagged =  not self.board.board_list[mx][my].flagged

                if self.check_win():
                    self.win = True
                    self.playing = False
                    for row in self.board.board_list:
                        for tile in row:
                            if not tile.revealed:
                                tile.flagged = True

    def end_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

#Runs the game even when losing
#Once game.run stops running it stops the whole process
game = Game()
while True:
    game.new()
    game.run()
   