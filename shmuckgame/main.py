from settings import *
import pygame as pg
import random
from player import *
from enemy import *
from animations import *
from powerup import *


# hud methods
font_name = pg.font.match_font("Comic Sans Ms")
def draw_text(surf,text,size,x,y,color):
    font = pg.font.Font(font_name,size)
    text_surf = font.render(text,True,color)
    text_rect = text_surf.get_rect()
    text_rect.midtop =(x,y)
    surf.blit(text_surf,text_rect)

#health bar
def draw_bar(surf,x,y,pct):
    if pct < 0:
        pct = 0
    bar_height = 25
    bar_length = 200
    fill = (pct/100)*bar_length
    outline_rect = pg.Rect(x,y,bar_length,bar_height)
    fill_rect = pg.Rect(x,y,fill,bar_height)
    pg.draw.rect(surf,GREEN,fill_rect)
    pg.draw.rect(surf,WHITE,outline_rect,3)

def draw_lives(surf,x,y,lives,img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x+ (img.get_width()+5) * i
        img_rect.y = y
        surf.blit(img,img_rect)

def show_gameover_screen():
    screen.blit(background,background_rect)
    draw_text(screen,TITLE,80,WIDTH/2,HEIGHT/4,RED)
    draw_text(screen, "arrow keys to move, spacebar to fire",30,WIDTH/2,HEIGHT/2,WHITE)
    draw_text(screen,"press any key to play or click the x to close",20,WIDTH/2,HEIGHT*3/4,BLUE)
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYUP:
                waiting = False



# setup pygame
pg.init()
pg.mixer.init()# setup sound


#creating game object
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Shmup!")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()
pow_group  = pg.sprite.Group()

#load imgs
background = pg.image.load(os.path.join(img_folder," ")).convert()
background = pg.transform.scale(background,(WIDTH,HEIGHT))
background_rect = background.get_rect()

player_img = pg.image.load(os.path.join(img_folder,"playerShip_blue,png")).convert()
player_mini_img = pg.transform.scale(player_img,(40,35))
player_mini_img.set_colorkey(BLACK)

bullet_img = pg.image.load(os.path.join(img_folder,"")).convert()

meteor_img_list = []
metoer_list = ["meteorBrown_1","meteorBrown_2","meteorBrown_3","meteorBrown_4",
               "meteorBrown_med1","meteorBrown_med3","meteorBrown_small1",
               "meteorBrown_small2","meteorBrown_tiny1","meteorBrown_tiny2",
               "meteorGrey_big1","meteorGrey_big2","meteorGrey_big3","meteorGrey_big4",
               "meteorGrey_med1","meteorGrey_med2","meteorGrey_small1","meteorGrey_small2","meteorGrey_tin1",
               "meteorGrey_tiny2"]

for img in metoer_list:
    meteor_img_list.append(pg.image.load(os.path.join(img_folder,img)).convert())


exp_anim = {}
exp_anim["lg"] = []
exp_anim["sm"] = []
exp_anim["playerExp"] = []
for i in range(9):
    filename = "regularExplosion0{}.png".format(i)
    img = pg.image.load(os.path.join(img_folder,filename)).convert()
    img.set_colorkey(BLACK)
    #large exp
    img_lg = pg.transform.scale(img,(75,75))
    exp_anim["lg"].append(img_lg)
    #small exp
    img_sm = pg.transform.scale(img,(30,30))
    exp_anim["sm"].append(img_sm)
    #player exp
    filename = "sonicExplosion0{}.png".format(i)
    img = pg.image.load(os.path.join(img_folder, filename)).convert()
    img.set_colorkey(BLACK)
    exp_anim["playerExp"].append(img)

pow_img = {}
pow_img["shield"] = pg.image.load(os.path.join(img_folder,"shield_gold.png")).convert()
pow_img["gun"] = pg.image.load(os.path.join(img_folder,"bolt_gold.png")).convert()



# loading in sound effects
shoot_fx = pg.mixer.Sound(os.path.join(fx_folder,"pew.wav"))
exp_name = ["Explosion3.wav"]
expsnd=[]
for snd in exp_name:
    expsnd.append(pg.mixer.Sound(os.path.join(fx_folder,snd)))
music = pg.mixer.music.load(os.path.join(music_folder,"music.ogg"))
pg.mixer.music.set_volume(0.4)
#powerup sound
pow_snd = pg.mixer.Sound(os.path.join(fx_folder,""))

#create player object
score = 0
player = Player(player_img,bullet_img,all_sprites,bullet_group,shoot_fx)

for i in range(20):
    e = Mob(random.choice(meteor_img_list))
    enemy_group.add(e)
    all_sprites.add(e)


# add all sprites to groups
all_sprites.add(player)
player_group.add(player)



running =True
game_over = True
pg.mixer.music.play(loops=-1)

#game loop
while running:
    if game_over:
        show_gameover_screen()
        game_over = False
        all_sprites = pg.sprite.Group()
        player_group = pg.sprite.Group()
        enemy_group = pg.sprite.Group()
        bullet_group = pg.sprite.Group()
        player = Player(player_img,bullet_img,all_sprites,bullet_group,shoot_fx)
        for i in range(20):
            e = Mob(random.choice(meteor_img_list))
            enemy_group.add(e)
            all_sprites.add(e)
        all_sprites.add(player)
        player_group.add(player)
        score = 0


    #tick clock
    clock.tick(FPS)
    # process events
    #collision with player an astroids
    hits = pg.sprite.spritecollide(player,enemy_group,True,pg.sprite.collide_circle)
    if hits:
        for hits in hits:
            if hit.radius >= 30:
                size = "lg"
            else:
                size = "sm"
            all_sprites.add(Explosion(size,exp_anim,hit.rect.center))
            random.choice(expsnd).play()
            player.takedamage(hit)
            e = Mob(random.choice(meteor_img_list))
            enemy_group.add(e)
            all_sprites.add(e)

            if player.shield <= 0:
                death_exp = Explosion("playerExp",exp_anim,player.rect.center)
                all_sprites.add(death_exp)
                player.die()

    if not player.lives == 0 and not death_exp.alive():
        game_over = True


            # damage player
            # destroy astroids
            # spawn replacement
    #check for collistion between bullets and astroids
    hits = pg.sprite.groupcollide(enemy_group,bullet_group,True,True)
    if hits:
        for hits in hits:
            score += int(50 - hit.radius)
            e = Mob(random.choice(meteor_img_list))
            enemy_group.add(e)
            all_sprites.add(e)
            if hit.radius >= 30:
                size = "lg"
            else:
                size = "sm"
            all_sprites.add(Explosion(size,exp_anim,hit.rect.center))
            random.choice(expsnd).play()
            if random.random() > 0.9:
                pow = Pow(hit.rect.center,pow_img)
                all_sprites.add(pow)
                pow_group.add(pow)

    # if player gets a powerup
    hits = pg.sprite.spritecollide(player,pow_group,True)
    if hits:
        for hits in hits:
            pow_snd.play()
            if hit.type == "shield":
                amount = random.randint(25,80)
                player.addShield(amount)

            if hit.type == "gun":
                player()


    for event in pg.event.get():

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot(bullet_img,all_sprites,bullet_group)
                shoot_fx.play()

        if event.type == pg.QUIT:
            running = False

    #update
    all_sprites.update()
    #process events
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot(bullet_img,all_sprites,bullet_group)
                shoot_fx()


        # if we clicked the X on the window
        if event.type == pg.QUIT:
            running = False



    #update
    all_sprites.update()

    #render/draw
    screen.fill(BLACK)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)


    #draw hud elements
    draw_text(screen,str(score),25,WIDTH/2,25,WHITE)

    draw_bar(screen,25,25,player.shield,GREEN)
    draw_text(screen,"shields",25,125,20,WHITE)

    draw_bar(screen, 25, 25, player.fuel,BLUE)
    draw_text(screen, "fuel", 25, 125, 20, WHITE)

    draw_lives(screen,WIDTH-100,25,player.lives)

    pg.display.flip()








