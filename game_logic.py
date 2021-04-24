import pygame
from asteroid import  Asteroid
from settings import *

def check_gameover(player, asteroids):
    if player.lives == 0:
        player.update_highscore()
        game_reset(player, asteroids)
        return True



def level_up(player, asteroids):
    player.level += 1

    if len(asteroids) < 12:
        for i in range(3):
            asteroid = Asteroid()
        asteroids.append(asteroid)

def handle_asteroids(asteroids, player, screen):
    zähler = 1

    for asteroid in asteroids:
        asteroid.move()
        asteroid.bounce()
        asteroid.collide_with_player(player)
        zähler += 1
        asteroid.draw_asteroid(screen)

def game_reset(player, asteroids):
    reset_player(player)
    reset_asteroids(asteroids)

def reset_asteroids(asteroids):
        for i in range(1):
            asteroids.clear()

def reset_player(player):
    player.lives = 3
    player.level = 0
    player.x = SCREEN_WIDTH / 2
    player.y = SCREEN_HEIGHT / 2

