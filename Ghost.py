import pygame
import random
import math
from pygame import mixer
import glob
import time
#from pygame import display,movie

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()
    return os.path.join(base_path, relative_path)

width =700
hieght =700
pygame.init()

background02 =[pygame.transform.scale(pygame.image.load(r'birthday\002\000 (1).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (2).png'),(width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (3).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (4).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (5).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (6).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (7).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (8).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (9).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (10).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (11).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (12).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (13).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (14).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\002\000 (15).png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00000.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00001.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00002.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00003.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00004.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00005.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00006.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00007.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00008.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00009.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00010.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00011.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00012.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00013.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00014.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00015.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00016.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00017.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00018.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00019.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00020.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00021.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00022.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\03\IMG00023.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00000.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00001.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00002.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00003.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00004.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00005.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00006.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00007.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00008.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00009.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00010.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00011.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00012.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00013.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00014.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00015.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00016.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00017.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00018.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00019.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00020.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00021.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00022.png'), (width, hieght)),
                 pygame.transform.scale(pygame.image.load(r'birthday\04\IMG00023.png'), (width, hieght))]
#print('02===',len(background02))

background05 =[pygame.transform.scale(pygame.image.load(r'birthday\02\000.png'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\00.png'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\01.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\02.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\03.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\04.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\05.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\06.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\07.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\08.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\10.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\11.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\12.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\13.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\14.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\15.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\16.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\17.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\18.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\19.jpg'),(width, hieght)),
               pygame.transform.scale(pygame.image.load(r'birthday\02\20.jpg'),(width, hieght))]
#print('05 ===',len(background05))

background_level_00 = pygame.transform.scale(pygame.image.load(r'back_ground_images\back_stage_01.jpg'),(width, hieght))
background_level_01 = pygame.transform.scale(pygame.image.load(r'back_ground_images\back_stage_02.jpg'),(width, hieght))
background_level_02 = pygame.transform.scale(pygame.image.load(r'back_ground_images\back_stage_03.jpg'),(width, hieght))
background_level_03 = pygame.transform.scale(pygame.image.load(r'back_ground_images\bisou.jpg'),(width, hieght))


image_background = r'back_ground_images\back_ground.png'
# create a screen
screen = pygame.display.set_mode((width, hieght))
# load teh image in the game background
back_ground = pygame.transform.scale(pygame.image.load(image_background),(width, hieght))

# Tiltle and icom

pygame.display.set_caption("GHOST's KINGDOM")
icon = pygame.image.load(r'back_ground_images\hb.ico')
pygame.display.set_icon(icon)

# player image
player_image = pygame.image.load(r'back_ground_images\player.png')
X_player = width/2-40
Y_player = hieght-200
changes_in_x = 0

# image of game over
image_game_over= r'back_ground_images\smurf_bk.png'
game_over_background = pygame.transform.scale(pygame.image.load(image_game_over), (width, hieght))

# score function
score_value = 0
font = pygame.font.Font(r'fonts\duskdemonrotate2.ttf',32)
game_over_font = pygame.font.Font(r'fonts\duskdemonrotate2.ttf',64)
second_chance_font= pygame.font.Font(r'fonts\duskdemonrotate2.ttf',32)
X_text = 0
Y_text= 0
life_chances= 0
next_level_value = 0
color= (0,255,0)
game_over_color=(0,0,0)
YOU_WON_color=(0,0,0)

stage_score=100
stage_score01=20
stage_score02=50
stage_score03=70


enemy_image=[]
X_enemy=[]
Y_enemy=[]
enemy_changes_in_an_x=[]
enemy_changes_in_an_y=[]
q=0
enemy_changes_in_an_x_value= q+1

list_of_ghosts=['ghosts/Besma.png',
                'ghosts/Hassan.png',
                'ghosts/Hitori.png',
                'ghosts/Iman.png',
                'ghosts/Marwa.png',
                'ghosts/Ritage.png',
                'ghosts/Sama.png',
                'ghosts/Yassine.png',
                'ghosts/king.png']

numb_of_anemies = len(list_of_ghosts)

bollet_image = pygame.image.load(r'back_ground_images\bollet_image.png')
X_bollet = 0
#print("x enmey =",X_bollet)
Y_bollet = hieght-200
bollet_changes_in_an_x = 0
bollet_changes_in_an_y = 4
bollet_state="ready"
bulette_num = 0

for i in range(len(list_of_ghosts)):
    # enemy image
    enemy_image.append(pygame.image.load(list_of_ghosts[i]))
    X_enemy.append(random.randint(0,width-64))
    Y_enemy.append(random.randint(10,50))
    enemy_changes_in_an_x .append(20)
    enemy_changes_in_an_y.append(20)

def show_text(x,y,color):
    global score,second_chanceses,netx_level
    score = font.render("Score: {}".format(score_value), True,color)
    second_chanceses = font.render("{} lives".format(life_chances), True,color)
    netx_level = font.render(" Level: {} ".format(next_level_value), True,color)
    screen.blit(score, (x, y))
    screen.blit(second_chanceses, (width-second_chanceses.get_width(),0))
    screen.blit(netx_level, ((width - netx_level.get_width())/2, 0))

def second_chance():
    global score_value,life_chances
    life_chances -= 1
    score_value-=10
    second_chance = mixer.Sound(r'Sounds\second_chance.mp3')
    second_chance.play()

def next_level():
    global next_level_value
    next_level_value+=1
    second_chance = mixer.Sound(r'Sounds\second_chance.mp3')
    second_chance.play()

def show_text_game_over(game_over_color):
    game_over_text = game_over_font.render(f"GAME OVER! {score_value}", True,game_over_color)
    screen.blit(game_over_text, ((width-game_over_text.get_width())/2,(hieght/2)-50))

def show_text_you_win(YOU_WON_color):

    you_win_text = game_over_font.render(f"YOU WON !!", True, YOU_WON_color)
    you_win_text1 = game_over_font.render(f"{bulette_num-score_value} missed Shots", True, YOU_WON_color)
    screen.blit(you_win_text, ((width-you_win_text.get_width())/2,hieght/2-250))
    screen.blit(you_win_text1, (((width-you_win_text1.get_width())/2,(hieght/2)-185)))

def game_over():
    global color,game_over_color,game_over
    game_over_color=(0,255,255)
    mixer.music.pause()
    game_over = mixer.Sound(r'Sounds\game_overr (3).wav')
    game_over.play()

def you_win():
    global color, YOU_WON_color,X_player,Y_player
    YOU_WON_color = (255, 0, 255)
    X_player=2000
    Y_player=2000
    mixer.music.pause()
    game_over = mixer.Sound(r'Sounds\Happy Birthday sweet sixteen6.mp3')
    game_over.play()

# player function
def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y,i):
    screen.blit(enemy_image[i], (x, y))

def fire_bollet(x,y):
    global bollet_state
    bollet_state="fire"
    screen.blit(bollet_image,(x+30,y))

# collision function
def is_collision(X_enemy,Y_enemy,X_bollet,Y_bollet):
    deistance = math.sqrt((math.pow((X_enemy-X_bollet),2)) + (math.pow((Y_enemy-Y_bollet),2)))
    if deistance<35:
        return True
    else:

        return False

def main():
    global X_player,X_enemy,X_text,X_bollet,YOU_WON_color,Y_enemy,Y_text
    global Y_bollet,Y_player,x,y,changes_in_x,bollet_changes_in_an_x,enemy_changes_in_an_y,score_value
    global bollet_state,life_chances,bollet_changes_in_an_y,enemy_changes_in_an_x,game_over,bulette_num,enemy_changes_in_an_x_value
    # background sound
    mixer.music.load(r"Sounds\Synthwave Robot Fabrik - Royalty Free Music.mp3")
    mixer.music.play(-1)
    win =0
    lose= 0
    timer = 0
    k=0
    running = True
    # game loop
    while running:
        screen.fill((0, 0, 0))
        #screen.blit(background01[k%5], (0, 0))
        screen.blit(background_level_00, (0, 0))
        k += 1
    # if the player is wining
        if win ==1:
            if timer<3*len(background02):
                screen.blit(background02[timer%len(background02)], (0, 0))
                time.sleep(.1)

            if timer < 50:
                show_text_you_win(YOU_WON_color)

            if timer>3*len(background02) :
                screen.blit(background05[timer%len(background05)], (0, 0))
                if timer%len(background05)==0:
                    time.sleep(9)
                else:
                    time.sleep(3)

            timer += 1
            print("timer =======================", timer)
        # if the player lose
        if lose==1:
            screen.fill((0, 0, 0))
            screen.blit(game_over_background, (0, 0))
            show_text_game_over(game_over_color)
            # condition for the second level of game
        elif score_value> stage_score01 and score_value<stage_score02:
            #screen.fill((0, 0, 0))
            screen.blit(background_level_01, (0, 0))


        elif score_value> stage_score02 and score_value<stage_score03:
            #screen.fill((0, 0, 0))
            screen.blit(background_level_02, (0, 0))


        elif score_value> stage_score03 and score_value<stage_score:
            #screen.fill((0, 0, 0))
            screen.blit(background_level_03, (0, 0))

    # background screen
    # events reader
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
                #running = False
            # if key is pressed check weather is left or right

            if event.type == pygame.KEYDOWN:
                #print("key is pressed")
                if event.key == pygame.K_LEFT:
                    #print("left")
                    changes_in_x = - 3

                if event.key == pygame.K_RIGHT:
                   # print("right")
                    changes_in_x = 3


                    # bollet show
                 # release the bullet:
                #if event.key == pygame.K_SPACE:
                if event.key == pygame.K_UP:
                    if bollet_state is "ready":
                        bollet_sound = mixer.Sound(r'Sounds\Release.mp3')
                        bollet_sound.play()
                        #print("SPACE")
                        X_bollet = X_player
                        fire_bollet(X_bollet,Y_bollet)
                        bulette_num +=1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:

                        main_main()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    changes_in_x = 0

        # # border condition for player
        if X_player >= width - 65:
            X_player = width - 65

        if X_player < 0:
            X_player = 0
        X_player += changes_in_x
########################################################################################ENEMY MOUVEMENT###############################################################################
    # anemy mouvement and border condition for enemy
        for i in range(numb_of_anemies):

            if Y_enemy[i] >= hieght-200 and life_chances > 0 and Y_enemy[i] < 999:
                for j in range(numb_of_anemies):
                    Y_enemy[j] = 0
                second_chance()
                # the condition of lose is tha that the enmey y>400 and life chances are nulll and y enemy are inferior than 999
            if Y_enemy[i] >= hieght-200 and life_chances <= 0 and Y_enemy[i] < 999:
                for k in range(numb_of_anemies):
                    Y_enemy[k] = 2000
                    lose = 1
                game_over()
                # the condition of winnig is that the enmy y is between 400 and 1000
            if score_value == stage_score:
                for l in range(numb_of_anemies):
                    Y_enemy[l] = 2000
                    win = 1
                score_value += 1
                you_win()

# jumping from level to next leve #############################################################################################################################
            if score_value == stage_score01:
                for m in range(numb_of_anemies):
                    Y_enemy[m] = 0
                enemy_changes_in_an_y[i] = 20
                bollet_changes_in_an_y = q+5
                enemy_changes_in_an_x_value = q+1
                next_level()
                score_value += 1

            if score_value == stage_score02:
                for n in range(numb_of_anemies):
                    Y_enemy[n] = 0
                enemy_changes_in_an_y[i] = 40
                bollet_changes_in_an_y = q+6
                enemy_changes_in_an_x_value = q+2
                next_level()

                score_value += 1

            if score_value == stage_score03:
                for o in range(numb_of_anemies):
                    Y_enemy[o] = 0
                enemy_changes_in_an_y[i] = 50
                bollet_changes_in_an_y= q+7
                enemy_changes_in_an_x_value =q+3
                next_level()
                score_value += 1
                break

            X_enemy[i] += enemy_changes_in_an_x[i]

            if X_enemy[i]  <= 0:
                enemy_changes_in_an_x [i] = enemy_changes_in_an_x_value
                Y_enemy[i]  += enemy_changes_in_an_y[i]

            elif X_enemy[i]  >= width-65:
                enemy_changes_in_an_x [i] = -enemy_changes_in_an_x_value
                Y_enemy[i]  += enemy_changes_in_an_y[i]
                #print("enemy_changes_in_an_y ======================",Y_enemy,enemy_changes_in_an_y)
            # colison condition
            collision = is_collision(X_enemy[i] , Y_enemy[i] , X_bollet , Y_bollet )
            if collision and bollet_state =="fire" :
                collision_sound = mixer.Sound(r'Sounds\Explosion.mp3')
                collision_sound.play()
                Y_bollet = hieght-200
                bollet_state = "ready"
                score_value += 1
                #print(score_value)

                if (int(score_value)% 10) == 0 and score_value<=stage_score/2:
                    life_chances += 1
                    #print("life_chances", life_chances)

                X_enemy[i]  = random.randint(0, width-65)
                #print("x enmey =", X_enemy[i] )
                Y_enemy[i]  = random.randint(20, 50)
            enemy(X_enemy[i], Y_enemy[i], i)

########################################################################################ENEMY MOUVEMENT###############################################################################
        #
    # satage upgrade:


        #bollet mouvement
        if Y_bollet<0:
            Y_bollet= hieght-200
            bollet_state="ready"
        if bollet_state is "fire":
            fire_bollet(X_bollet,Y_bollet)
            Y_bollet-= bollet_changes_in_an_y
        player(X_player, Y_player)
        show_text(X_text,Y_text,color)
        pygame.display.update()



def main_main():
    global q

    run = True
    font_text = pygame.font.Font(r'fonts\duskdemonrotate2.ttf',80)
    font_text1 = pygame.font.Font(r'fonts\Outerlord Demo.ttf',40)
    font_text2 = pygame.font.Font(r'fonts\Vientien-Normal.ttf', 25)
    font_text3 = pygame.font.Font(r'fonts\Standrag.otf', 30)

    easy_color =(0, 255, 0)
    medium_color =  (255, 255, 0)
    hard_color = (255, 0, 0)
    selected_color= (255, 0, 255)

    while run:
        screen.blit(back_ground,(0,0))
        text_label0 = font_text1.render("FROM YASSINE TO MY DEAR SISTER BELKIS", True, (255, 0, 255))
        screen.blit(text_label0, (((width - text_label0.get_width()) / 2), (0)))

        text_label = font_text3.render("E: Easy", True, easy_color )
        screen.blit(text_label, (0, (hieght / 2) - 300))
        text_label = font_text3.render("M: Medium", True,medium_color)
        screen.blit(text_label, (0, (hieght / 2) - 270))
        text_label = font_text3.render("H: Hard", True, hard_color)
        screen.blit(text_label, (0, (hieght / 2) - 240))


        text_label = font_text.render("Press ENTER ",True,(0,0,255))
        screen.blit(text_label,(((width-text_label.get_width())/2),(hieght/2)-100))
        text_label1 = font_text.render("to START the game!", True, (0, 0, 255))
        screen.blit(text_label1, (((width - text_label1.get_width()) / 2), (hieght/ 2)))
        text_label2 = font_text2.render("DEVELOPED BY :", True, (160, 0, 0))
        screen.blit(text_label2, (((width - text_label2.get_width()) / 2), (hieght-80)))
        text_label2 = font_text2.render("BOUZID YASSINE METLILI GHARDAIA ALGERIA 2020", True, (0, 255, 0))
        screen.blit(text_label2, (((width - text_label2.get_width()) / 2), (hieght - 50)))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    q=0
                    easy_color = selected_color
                    medium_color = (255, 255, 0)
                    hard_color = (255, 0, 0)
                    print("easy game",q)
                if event.key == pygame.K_m:
                    q=1
                    easy_color = (0, 255, 0)
                    medium_color = selected_color
                    hard_color = (255, 0, 0)
                    print("meduim game", q)
                if event.key == pygame.K_h:
                    q=2
                    easy_color = (0, 255, 0)
                    medium_color = (255, 255, 0)
                    hard_color =selected_color

                    print("hard game",q)
                if event.key == pygame.K_RETURN:
                    main()
    pygame.quit()

main_main()
