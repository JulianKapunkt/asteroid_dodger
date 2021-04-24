import pygame, sys
from random import randint, uniform, choice
from settings import *

class Asteroid:

    def __init__(self):
        self.speed_y = uniform(0.0,2.5) * choice((-1,1))
        self.speed_x = uniform(0.0,2.5) * choice((-1,1))
        self.color = LIGHT_GREY
        self.size = randint(20, 40)
        self.starting_positions = ((-100, randint(0, SCREEN_HEIGHT)), (SCREEN_WIDTH + 100, randint(0, SCREEN_HEIGHT)), (randint(0, SCREEN_WIDTH), -100), (randint(0,SCREEN_WIDTH), SCREEN_HEIGHT+100))
        self.x = randint(0 + self.size, SCREEN_WIDTH - self.size)
        self.y = randint(0 + self.size, SCREEN_HEIGHT - self.size)
        self.shape = pygame.Rect(self.x, self.y, self.size, self.size)
        self.color = choice(COLORS)

    def draw_asteroid(self, screen):
        self.shape = pygame.Rect(self.x, self.y, self.size, self.size)
        #pygame.draw.rect(screen, "black", self.shape)
        pygame.draw.circle(screen, self.color,(self.x + self.size/2, self.y+ self.size/2), self.size /2)
        pygame.draw.circle(screen, "white", (self.x+ self.size/2, self.y+ self.size/2), self.size /2, width=3)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce(self):
        if self.x < 0:
            self.speed_x *= -1
        if self.x > SCREEN_WIDTH - self.size:
            self.speed_x *= -1
        if self.y < 0:
            self.speed_y *= -1
        if self.y > SCREEN_HEIGHT - self.size:
            self.speed_y *= -1

    def hide(self):
        self.x, self.y = choice(self.starting_positions)
        tupel= (self.x, self.y)
        print(tupel)

    def collide_with_player(self, player):
        if self.shape.colliderect(player.hitbox):
                player.lives -= 1
                self.hide()






