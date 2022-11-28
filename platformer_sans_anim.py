# Import dependencies
import pygame, sys
from pygame.locals import *
import spritesheet
import random

# Starting your engines
pygame.init()

# Setting the FPS
FPS = 60
FramePerSec = pygame.time.Clock()

#background
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
BG = (50,50,50)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer")

player_sprite_sheet = pygame.image.load('Documents/Code/Python/Pygame/platformer/assets/characters/player.png').convert_alpha()
player_sheet = spritesheet.SpriteSheet(player_sprite_sheet)
player_sprite = player_sheet.get_image(0, 0, 48, 48, 3, (0,0,0))

# Colors

# Creating a player class, built off the PyGame base sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_sprite
        self.rect = self.image.get_rect()
    
    def jump(self):
        pass
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        #print(pressed_keys)
        if pressed_keys[K_RIGHT]: # right
            #print("right")
            if self.rect.x + self.rect.width <= 790:
                self.image = player_sprite
                self.rect.move_ip(5, 0)
        elif pressed_keys[K_LEFT]: # left
            #print("left")
            if self.rect.x >= 5:
                self.image = pygame.transform.flip(player_sprite.convert_alpha(), True, False)
                self.rect.move_ip(-5, 0)
        elif pressed_keys[K_UP]: # up
            #print("up")
            if self.rect.y >= 5:
                self.rect.move_ip(0, -5)
        elif pressed_keys[K_DOWN]: # down
            #print("down")
            if self.rect.y + self.rect.height <= 590:
                self.rect.move_ip(0, 5)
        else:
            pass
            #print("idle")
                
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Instantiating (making exist) a player
player1 = Player()



# THE GAME LOOP
while True:		   
    for event in pygame.event.get():              
        # Checking if player wants to quit
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()  
    screen.fill(BG)
    
    player1.draw(screen)
    player1.update()
    #screen.blit(movement_frames[frame], (100, 100))
		
    pygame.display.update()
    FramePerSec.tick(FPS)