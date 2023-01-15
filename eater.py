import pygame
from pygame.locals import *
import sys
import random, time

# Initialise

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
you_scored = font_small.render("Points scored:", True, BLACK)


# Load background

background = pygame.image.load("background.png")
title = pygame.image.load("title.png")

# Set up display

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Healthy Eater")

# Create sprites

class Burger(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("burger.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            
        
        
class Lettuce(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lettuce.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            
        
            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("robin.jpg")
        self.rect = Rect(0,0,50, 10)
        self.rect.center = (160, 520)

    def move(self):
        
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < SCREEN_WIDTH :
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        
            
# Setting up sprites
P1 = Player()
E1 = Burger()
F1 = Lettuce()

# Creating sprite groups

players = pygame.sprite.Group()
players.add(P1)
burgers = pygame.sprite.Group()
burgers.add(E1)
lettuces = pygame.sprite.Group()
lettuces.add(F1)


# Adding a new User Event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

food = random.choice((burgers, lettuces))

            
def main():
    
    global SCORE, food, SPEED

    while True:
        for event in pygame.event.get():
            
            if event.type == INC_SPEED:
                SPEED += 0.2
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAYSURF.blit(background, (0, 0))
        scores = font_small.render(str(SCORE), True, RED)
        DISPLAYSURF.blit(scores, (10, 10))
    
    # Moves and redraws all sprites
    
        
        for entity in food:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
            if (entity.rect.top >= 590):
                food = random.choice((burgers, lettuces))
        
        for entity in players:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()       

            
       
    

    # To be run if collision occurs between Player and Burger
    
        if pygame.sprite.spritecollideany(P1, burgers):
            pygame.mixer.Sound("burrp.wav").play()
            time.sleep(0.5)
        
            DISPLAYSURF.fill(BLUE)
            DISPLAYSURF.blit(game_over, (30, 250))
            DISPLAYSURF.blit(you_scored, (30, 340))
            DISPLAYSURF.blit(scores, (200, 340))
            
            pygame.display.update()
            
            for entity in players:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        
        if pygame.sprite.spritecollideany(P1, lettuces):
            SCORE += 1
            for entity in lettuces:
                entity.kill()
                entity.rect.top = 600
                lettuces.add(F1)
                food = random.choice((burgers, lettuces))
              
                  

        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == '__main__':
    main()
