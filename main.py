from random import randint

from pygame import *
window =display.set_mode((800,600))
space = transform.scale(image.load("galaxy.jpg"), (800,600))

mixer.init()
mixer.music.load('space.ogg')
fire_sound =mixer.Sound("fire.ogg")

clock=time.Clock()
FPS = 40
clock.tick(FPS)

class GameSprite(sprite.Sprite):
    def __init__(self,pacman,x,y,speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(pacman),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
    def reset (self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x< 800-85:
            self.rect.x +=self.speed
        if keys_pressed[K_a] and self.rect.x> 0:
            self.rect.x -= self.speed
    def fire(self):
        bullet = Bullet("bullet.png" , self.rect.centerx, self.rect.top,-15,15,20)
        bullets.add(bullet)
lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y +=self.speed
        global lost
        if self.rect.y > 600:
            self.rect.y=0
            self.rect.x= randint(0,700)
            lost = lost+1
bullets =  sprite.Group()

class Bullet(GameSprite):
    def update(self):
        self.rect.y +=self.speed
        global lost
        if self.rect.y <=0:
            self.kill()



game = True
finish = False
player = Player("rocket.png", 0,400,9,80,100)
enemy = Enemy("ufo.png",randint(0,700),0,3,80,50)
enemy2 = Enemy("ufo.png",randint(0,700),0,2,80,50)
enemy3= Enemy("ufo.png",randint(0,700),0,3,80,50)
enemy4 = Enemy("ufo.png",randint(0,700),0,2,80,50)
enemy5 = Enemy("ufo.png",randint(0,700),0,1,80,50)
monsters = sprite.Group()
monsters.add(enemy)
monsters.add(enemy2)
monsters.add(enemy3)
monsters.add(enemy4)
monsters.add(enemy5)
font.init()
bis = 0
font1 =font.SysFont('Arial',36)
while  game:


    text_lose = font1.render("Пропуск:" + str(lost),1,(255,255,255))
    bistro = font1.render("Пристреленно:" + str(bis), 1, (255, 255, 255))
    fly = font1.render("Хороооооош" , 1 ,(255,255,255))
    loose = font1.render("Ай яй яй !!!", 1,(255,255,255))
    for e in event.get():
        if QUIT == e.type:
            game = False
        elif e.type==KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                player.fire()
    collides = sprite.groupcollide(monsters,bullets,True,True)


    for i in collides:
        enemy4 = Enemy("ufo.png", randint(0, 700), 0, 2, 80, 50)
        monsters.add(enemy4)
        bis = bis +1

    if finish != True:
        window.blit(space, (0, 0))
        player.update()
        player.reset()
        bullets.update()
        bullets.draw(window)
        monsters.update()
        monsters.draw(window)
    window.blit(text_lose,(0,0))
    window.blit(bistro,(0,30))
    if lost>=34:
        finish = True
        window.blit(fly,(450,250))
    if bis ==100:
        finish = True
        window.blit(fly,(300,350))


    clock.tick()
    display.update()