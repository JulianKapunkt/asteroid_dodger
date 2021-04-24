import pygame
from settings import *

class Anzeige():

    def __init__(self):
        self.color = LIGHT_GREY
        self.GAME_FONT = pygame.font.Font("freesansbold.ttf",30)

    # def print_lives(self, screen, lives):
    #     verbleibende_leben = self.GAME_FONT.render(f"Lives: {lives}", True, LIGHT_GREY)
    #     screen.blit(verbleibende_leben, (45, 20))

    def print_score(self, screen, score):
        spielstand = self.GAME_FONT.render(f"Level: {score}", True, LIGHT_GREY)
        screen.blit(spielstand, (45, 20))

    def print_highscore(self, screen, player):
        highscore = self.GAME_FONT.render(f"Highscore: {player.highscore}", True, LIGHT_GREY)
        screen.blit(highscore, (45, 50))

    # def print_time_remaining(self, screen, time_remaining):
    #     timer = self.GAME_FONT.render(f"Time: {time_remaining}", True, LIGHT_GREY)
    #     screen.blit(timer, (45, 80))

    def print_game_over(self, screen, level, timer):
        if timer > 0:
            game_over = self.GAME_FONT.render(f"Game Over!", True, "white")
            screen.blit(game_over, (SCREEN_WIDTH/2 - 160, SCREEN_HEIGHT/2 - 60))

    def print_bomb(self, screen, player):
        bombs = self.GAME_FONT.render(f"Bombs: {player.bombs}", True, LIGHT_GREY)
        screen.blit(bombs, (45, 110))



