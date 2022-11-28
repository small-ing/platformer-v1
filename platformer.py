# Import dependencies
import pygame, sys
import spritesheet
from pygame.locals import *
import random

# Starting your engines
pygame.init()

# Setting the FPS
FPS = 60
frame = 0
FramePerSec = pygame.time.Clock()
last_update = pygame.time.get_ticks()

animation_cooldown = 250

#background
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
BG = (50,50,50)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer")

# Colors

# spritesheet
player_sprite_sheet = pygame.image.load('Documents/Code/Python/Pygame/platformer/assets/characters/player.png').convert_alpha()
player_sheet = spritesheet.SpriteSheet(player_sprite_sheet)
# Creating a player class, built off the PyGame base sprite class
class Player(pygame.sprite.Sprite):
    action = 0
    jumping = False
    jump_counter = 0
    idle_frames = []
    for i in range(6):
        idle_frames.append(player_sheet.get_image(0, i, 48, 48, 3, (0,0,0)))
        
    movement_frames = []
    for i in range(12):
        if i < 6:
            movement_frames.append(player_sheet.get_image(1, i, 48, 48, 3, (0,0,0)))    
        else:
            movement_frames.append( pygame.transform.flip(player_sheet.get_image(1, i-6, 48, 48, 3, (0,0,0)).convert_alpha(), True, False) )
    
    def __init__(self):
        super().__init__()
        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 525)
    
    def jump(self):
        self.jumping = True

    
    def update(self):
        if self.rect.y < 450 and not self.jumping:
            self.rect.move_ip(0, 5)
        elif self.jumping:
            self.rect.move_ip(0, -5)
            self.jump_counter += 1
            if self.jump_counter > 25:
                self.jumping = False
                self.jump_counter = 0
        pressed_keys = pygame.key.get_pressed()
        #print(pressed_keys)
        if pressed_keys[K_RIGHT]: # right
            #print("right")
            if self.rect.x + self.rect.width <= 790:
                self.action = 1
                self.rect.move_ip(5, 0)
        elif pressed_keys[K_LEFT]: # left
            #print("left")
            if self.rect.x >= 5:
                self.action = 2
                self.rect.move_ip(-5, 0)
        #elif pressed_keys[K_UP]: # up
            #print("up")
        #    if self.rect.y >= 5:
        #        self.action = 1
        #        self.rect.move_ip(0, -5)
        #elif pressed_keys[K_DOWN]: # down
            #print("down")
        #    if self.rect.y + self.rect.height <= 590:
        #        self.action = 2
        #        self.rect.move_ip(0, 5)
        else:
            #print("idle")
            self.action = 0
                
    def draw(self, surface, frame):
        if self.action == 0:
            surface.blit(self.idle_frames[frame], self.rect)
        elif self.action == 1:
            surface.blit(self.movement_frames[frame], self.rect)
        elif self.action == 2:
            surface.blit(self.movement_frames[frame + 6], self.rect)
        else:
            surface.blit(self.idle_frames[frame], self.rect)

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
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:
                player1.jump()
    screen.fill(BG)
    
    # frame counter for animations
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= 6:
            frame = 0

    pygame.draw.rect(screen, (65, 65, 65), pygame.Rect(0,500,800,100))
    
    player1.draw(screen, frame)
    player1.update()
    
    #screen.blit(movement_frames[frame], (100, 100))
		
    pygame.display.update()
    FramePerSec.tick(FPS)