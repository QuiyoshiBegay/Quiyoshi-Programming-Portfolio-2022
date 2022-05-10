from settings import *
import pygame as pg
import random

class Mob(pg.sprite.Sprite):
    def __init__(self,sprite):
        super(Mob, self).__init__()
        self.image_orig = sprite
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        #self.image = pg.transform.scale(scale.image,(50,50))

        self.rect = self.image.get_rect()
        self.radius = (self.rect.width * .8) /2
        #pg.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.centerx = random.randint(20, WIDTH-20)
        self.rect.bottom = random.randint(-25, 0)
        self.speed_x = random.randint(-3.3)
        self.speed_y = random.randint(4,12)
        self.rot =0
        self.rot_speed = random.randint(-8,8)
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot+self.rot_speed)%360
            new_img =pg.transform.rotate(self.image_orig,self.rot)
            old_center =self.rect.center
            self.image = new_img
            self.rect = self.image.get_rect()
            #self.rect.center

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update> self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.exp_anim[self.size]):
                self.kill()

        else:
            center = self.rect.center
            self.image = self.exp_anime[self.size][self.frane]
            self.rect = self.image.get_rect()
            self.rect.center = center