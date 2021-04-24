from settings import *
import  pygame


class Player:

    def __init__(self):
        self.x_speed = 4
        self.y_speed = 4
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2
        self.color = LIGHT_GREY
        self.size = 50
        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.size)
        self.lives = 3
        self.level = 0
        self.bombs = 1
        with open("highscore.txt", mode="r") as data:
            self.highscore = int(data.read())

    def control_player(self, pressed, asteroids):
        if pressed[pygame.K_LEFT] and self.hitbox.left > 0:
            self.x -= self.x_speed
        if pressed[pygame.K_RIGHT] and self.hitbox.right < SCREEN_WIDTH:
            self.x += self.x_speed
        if pressed[pygame.K_UP] and self.hitbox.top > 0:
            self.y -= self.y_speed
        if pressed[pygame.K_DOWN] and self.hitbox.bottom < SCREEN_HEIGHT:
            self.y += self.y_speed
        if pressed[pygame.K_SPACE] and self.bombs > 0:
            self.detonate_bomb(asteroids)

    def update_highscore(self):
        if self.level > self.highscore:
            self.highscore = self.level
        with open("highscore.txt", mode="w") as data:
            data.write(f"{self.highscore}")

    def draw_player(self, screen):
        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.size)
        if self.lives > 1:
            pygame.draw.circle(screen, "white", (self.x + self.size/2, self.y + self.size/2), self.size /2 + 10, width=3)
        if self.lives > 2:
            pygame.draw.circle(screen, "white", (self.x + self.size/2, self.y + self.size/2), self.size , width=3)

        #TODO: Delete when Finished
        #pygame.draw.rect(screen, "black", self.hitbox)
        if self.bombs > 0:
            pygame.draw.circle(screen, "red", (self.x + self.size / 2, self.y + self.size/2 ), self.size/2)
        else:
            pygame.draw.circle(screen, "white", (self.x + self.size/2, self.y + self.size/2 ), self.size/2)

    def loose_life(self):
        self.lives -= 1

    def detonate_bomb(self, asteroids):
        self.bombs -= 1
        for i in range(1):
            asteroids.clear()



