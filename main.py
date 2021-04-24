import pygame, sys
from random import randint, choice
from settings import *
from asteroid import Asteroid
from player import Player
from game_logic import *
from anzeige import *

pygame.init()
clock = pygame.time.Clock()

#Setting up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Asteroid Dodger')

asteroids = []
player = Player()
anzeige = Anzeige()

time_remaining = 100
timer = 0

for i in range(2):
    print(asteroids)
    asteroid = Asteroid()
    asteroids.append(asteroid)

print(asteroids)

game_running = True
#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed_key = pygame.key.get_pressed()
    player.control_player(pressed_key, asteroids)
    time_remaining -= 1
    timer -= 1

    #Level Up
    if time_remaining <= 0:
        level_up(player, asteroids)
        time_remaining = 100

    #Draw
    screen.fill(BG_COLOR)
    player.draw_player(screen)
    handle_asteroids(asteroids, player, screen)
    #anzeige.print_lives(screen, player.lives)
    anzeige.print_score(screen, player.level)
    #anzeige.print_time_remaining(screen, time_remaining)
    anzeige.print_bomb(screen, player)
    anzeige.print_highscore(screen, player)
    anzeige.print_game_over(screen, player.level, timer)
    print (timer)
    if check_gameover(player, asteroids):
        timer = 100
    pygame.display.flip()

    clock.tick(120)