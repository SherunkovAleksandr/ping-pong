from pygame import *
from random import randint

win_wight = 1200
win_hight = 800
speed = 6
speed_x = 7
speed_y = 7
FPS = 60
clock = time.Clock()
window = display.set_mode((win_wight, win_hight))
display.set_caption('ping_pong window')
background = transform.scale(image.load('---------------------------_5b615hhw.jpg'), (win_wight, win_hight))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Playear(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_hight - 80:
            self.rect.y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_hight - 80:
            self.rect.y += self.speed

player1 = Playear('png-transparent-pillar-wood-trunk-trees.png', 0, 300, speed, 100,130) 
player2 = Playear('png-transparent-pillar-wood-trunk-trees.png', 1100, 300, speed, 100,130)
ball = GameSprite('Tennis-Ball-PNG-HD-Quality.png', 500, 400,  speed, 50, 50)

run = True
finish = False

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (100,0,0))
lose2 = font1.render('PLAYER 2 Lose!', True, (100,0,0))


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background,(0, 0))

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_hight - 50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (420,100))

    if ball.rect.x > win_wight - 50:
        finish = True
        window.blit(lose2, (420,100))

    

    player1.update_l()
    player1.reset() 
    player2.update_r()
    player2.reset()
    ball.reset()

    clock.tick(FPS)
    display.update()   
