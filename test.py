from pygame import *
clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption("Пинг-понг")
speed = 10
background = transform.scale(image.load("background.jpg"), (700,500))
game = True
Fps = 90003000
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            #if finish != True: 
    window.blit(background,(0,0))
    clock.tick(Fps)
    display.update()