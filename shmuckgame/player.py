import pygame as pg
from settings import *
import random


class Player(pg.sprite.Sprite):
    def __init__(self,sprite,bullet_sprite,all_sprites,bullet_group,shootsnd):
        super(Player, self).__init__()
        self.image = pg.Surface((50,50))
        self.image = sprite
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = (self.rect.width *.8)/2
        # pg.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - self.rect.height
        self.dir_x = 0
        self.dir_y = 0
        self.moveSpeed = 8
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()
        self.all_sprites = all_sprites
        self.bullet_group = bullet_group
        self.bullet_sprite = bullet_sprite
        self.shootsnd = shootsnd
        self.lives = 3
        self.hidden = False
        self.hide_timer = pg.time.get_ticks()
        self.gun_power = 0



    def update(self):
        if self.hidden and pg.time.get_ticks() - self.hide_timer >1500:
            self.hidden = False
            self.rect.centerx = WIDTH /2
            self.rect.bottom = HEIGHT - self.rect.height
        # set speed back to 0
        self.speed_x = 0
        #get player movement
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speed_x = -self.moveSpeed
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speed_x = self.moveSpeed
        if keystate[pg.K_SPACE]:
            self.shoot(self.bullet_sprite,self.all_sprites,self.bullet_group)
        # binde player to screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            #update position
        self.rect.x += self.speed_x

    def shoot(self,sprite,all_sprites,bullet_group):
        now = pg.time.get_ticks()
        if now - self.last_shot>self.shoot_delay:
            self.last_shot = now
            self.shootsnd.play()
            if self.gun_power == 0:
                bullet = Bullet(self.rect.centerx,self.rect.top -5,sprite,all_sprites,bullet_group)
            elif self.gun_power == 1:
                self.shoot_delay = 175
                bullet = Bullet(self.rect.centerx, self.rect.top - 5, sprite, all_sprites, bullet_group)
            elif self.gun_power ==2:
                self.shoot_delay = 250
                bullet = Bullet(self.rect.left+2, self.rect.top, sprite, all_sprites, bullet_group)
                bullet = Bullet(self.rect.right-2, self.rect.top, sprite, all_sprites, bullet_group)
            elif self.gun_power ==3:
                self.shoot_delay = 250
                bullet = Bullet(self.rect.centerx, self.rect.top - 5, sprite, all_sprites, bullet_group)
                bullet = Bullet(self.rect.right+2, self.rect.top, sprite, all_sprites, bullet_group)
                bullet = Bullet(self.rect.right - 2, self.rect.top, sprite, all_sprites, bullet_group)
            elif self.gun_power ==4:
                self.shoot_delay = 275
                bullet = Bullet(self.rect.centerx, self.rect.top - 5, sprite, all_sprites, bullet_group)
                bullet = Bullet(self.rect.right+2, self.rect.top, sprite, all_sprites, bullet_group)
                bullet = Bullet(self.rect.right - 2, self.rect.top, sprite, all_sprites, bullet_group)
            elif self.gun_power ==5:
                self.shoot_delay = 100
                bullet = Bullet(self.rect.centerx+3, self.rect.top - 5, sprite, all_sprites, bullet_group)
                bullet = Bullet(self.rect.centerx-3, self.rect.top - 5, sprite, all_sprites, bullet_group)
                bullet = Bullet(self.rect.right+2, self.rect.top, sprite, all_sprites, bullet_group,-1)
                bullet = Bullet(self.rect.right - 2, self.rect.top, sprite, all_sprites, bullet_group,1)
                bullet = Bullet(self.rect.right + 2, self.rect.top, sprite, all_sprites, bullet_group,-3)
                bullet = Bullet(self.rect.right - 2, self.rect.top, sprite, all_sprites, bullet_group,3)


    def takedamage(self,hit):
        self.shield -= hit.radius
        self.gun_down()

    def die(self):
        self.lives -=1
        self.hide()
        self.shield = 100
        self.gun_down()

    def hide(self):
        self.hidden = True
        self.hide_timer = pg.time.get_ticks()
        self.rect.center = (WIDTH/2 ,HEIGHT+500)

    def addShield(self,amount):
        self.shield += amount
        if self.shield > self.max_shield:
            self.shield = self.max_shield

    def gun_up(self):
        if self.gun_power <0:
            self.gun_power = 0
        if self.gun_power >5:
            self.gun_power = 5
        self.gun_power +=1


class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y,sprite,all_sprites,bullet_group):
        super(Bullet, self).__init__()
        self.image = sprite
        self.image = pg.transform.scale(self.image,(10,20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = -12
        self.speed_x = 0
        all_sprites.add(self)
        bullet_group.add(self)

    def update(self):
        self.rect.centery += self.speed_y
        if self.rect.bottom <-5:
            self.kill()


