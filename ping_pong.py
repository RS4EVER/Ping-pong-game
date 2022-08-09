from pygame import *
init()
#создай окно игры
win_width = 700
win_height = 500
w = display.set_mode((win_width, win_height))
display.set_caption('Pin-pong')
#bg = transform.scale(image.load("bg.jpg"), (win_width, win_height))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        w.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_a] and self.rect.x < win_width-100:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-100:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-100:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-100:
            self.rect.y += self.speed

run = True
finish = False
FPS = 60
clock = time.Clock()
while run:
    #w.blit(bg, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        pass
    display.update()
    clock.tick(FPS)