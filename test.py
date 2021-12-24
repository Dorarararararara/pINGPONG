from pygame import *
clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption("Пинг-понг")
speed = 10
background = transform.scale(image.load("background.jpg"), (700,500))
game = True
Fps = 90003000
finish = False
speed_x = 3
speed_y = 5
win_height = 500
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size_x, player_size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_size_x, player_size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 440:
            self.rect.y += self.speed
gamer1 = Player("P1.png", 15, 250, 10, 40, 60)
gamer2 = Enemy("P2.png", 660, 250, 10, 40, 60)
ball = GameSprite("ball.png", 350, 250, 15, 20, 60)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False            
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        window.blit(background,(0,0))
        gamer1.reset()
        gamer2.reset()
        ball.reset()
        gamer1.update()
        gamer2.update()
        ball.update()
    clock.tick(Fps)
    display.update()