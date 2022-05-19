#Coordinates used in conditional statements correspond to speed (+ or - 2). Change in speed will require change if coordinates in all conditions for smooth functioning

import pygame
import random
import math
from pygame import mixer

screen_width=800
screen_height=600
BLACK=(0,0,0)

pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height),pygame.FULLSCREEN)

#background

bg_file='bg.jpg'
open_file='poster.jpg'
bg=pygame.image.load(bg_file)
open_img=pygame.image.load(open_file)

#icon

icon_file='icon.png'
icon=pygame.image.load(icon_file)

#bgm
mixer.music.load('bgm.wav')
mixer.music.play(-1)



#nest
nest_file0='nest0.png'
nest_file1='nest1.png'
nest_file2='nest2.png'
nest_file3='nest3.png'
nest_file4='nest4.png'
nest_file5='nest5.png'
nest_file6='nest6.png'
nest_file7='nest7.png'
nest_img0=pygame.image.load(nest_file0)
nest_img1=pygame.image.load(nest_file1)
nest_img2=pygame.image.load(nest_file2)
nest_img3=pygame.image.load(nest_file3)
nest_img4=pygame.image.load(nest_file4)
nest_img5=pygame.image.load(nest_file5)
nest_img6=pygame.image.load(nest_file6)
nest_img7=pygame.image.load(nest_file7)
nest_x=30
nest_y=45


#player

player_file='player.png'
player_mirror_file='player_mirror.png'
player_img=pygame.image.load(player_file)
playermirror_img=pygame.image.load(player_mirror_file)
player_x=250
player_y=88
player_globaly=88
player_changex=0
player_changey=0

#egg
egg_file='egg.png'
egg_xlist=[75,150,225,500,575,650]
egg_ylist1=[520,920]
egg_ylist2=[320,720]
num_of_eggs=7

egg_img=[]
egg_x=[]
egg_y=[]
egg_globaly=[]
egg_changex=[]
egg_changey=[]
egg_sound=[]


for i in range(num_of_eggs):
    egg_img.append(pygame.image.load(egg_file))
    egg_sound.append(True)
    egg_x.append(random.choice([75,150,225,500,575,650]))
    
    if egg_x[i]==75 or egg_x[i]==150 or egg_x[i]==225:
        egg_y.append(random.choice(egg_ylist1))
    elif egg_x[i]==500 or egg_x[i]==575 or egg_x[i]==650:
        egg_y.append(random.choice(egg_ylist2))
    egg_globaly.append(egg_y[i])
        

#score

font=pygame.font.Font('Space Quest.otf',16)
text_x=10
text_y=10
score_value=(num_of_eggs)

def show_score(x,y):
    score=font.render('Eggs: '+str(num_of_eggs-score_value), True, (255,255,255))
    more_eggs=font.render(str(score_value)+' more eggs to go', True, (255,255,255))
    screen.blit(score,(x,y))
    screen.blit(more_eggs,(x,y+20))

#gameover
over_font=pygame.font.Font('Space Quest.otf',72)
over_x=180
over_y=180

def game_over(x,y):
    over=over_font.render("GAME OVER", True, (255,255,255))
    restart=font.render("Press r to restart", True, (255,255,255))
    quitgame=font.render("Press esc to exit", True, (255,255,255))
    screen.blit(over,(x,y))
    screen.blit(restart,(x+120,y+100))
    screen.blit(quitgame,(x+127,y+130))

#win
win_font=pygame.font.Font('Space Quest.otf',72)
win_x=150
win_y=180
win_status=False

def win(x,y,t,s):
    u_win=win_font.render("WELL PLAYED!", True, (255,255,255))
    restart=font.render("Press r to restart", True, (255,255,255))
    quitgame=font.render("Press esc to exit", True, (255,255,255))
    time_left= font.render('Time taken: '+str(t)+' seconds', True, (255,255,255))
    score_achieved=font.render('Score: '+str(s)+'%', True, (255,255,255))
    screen.blit(u_win,(x,y))
    screen.blit(restart,(x+150,y+100))
    screen.blit(quitgame,(x+157,y+130))
    screen.blit(time_left,(x+112,y+160))
    screen.blit(score_achieved,(x+180,y+190))

#clock
time_running=False
clock1=pygame.time.Clock()
clock_font=pygame.font.Font('Space Quest.otf',16)
clock_x=750
clock_y=10
time_left=59
dt = 0

def show_clock(x,y):
    clock=clock_font.render("0:"+str(int(round(time_left,0))), True, (255,255,255))
    screen.blit(clock,(x,y))

#enemy
enemy_file='enemy.png'
enemy_mirror_file='enemy_mirror.png'
enemy_img=[]
enemy_mirror_img=[]
enemy_x=[]
enemy_y=[]
enemy_globaly=[]
enemy_changex=[]
enemy_changey=[]
num_of_enemies=6

for i in range(num_of_enemies):
    
    enemy_img.append(pygame.image.load(enemy_file))
    enemy_mirror_img.append(pygame.image.load(enemy_mirror_file))
    enemy_x.append(random.randrange(0,800))
    enemy_y.append(random.randrange(300,900))
    enemy_globaly.append(enemy_y[i])
    enemy_changex.append(2)
    enemy_changey.append(2)

pygame.display.set_icon(icon)
pygame.display.set_caption("Dragon Eggs")

def background(x,y):
    screen.blit(bg,(x,y))

def open(x,y):
    screen.blit(open_img,(x,y))

def egg(x,y,i):
    screen.blit(egg_img[i],(x,y))

def nest(nest_img,x,y):
    screen.blit(nest_img,(x,y))

def player(x,y):
    screen.blit(player_img,(x,y))

def player_mirror(x,y):
    screen.blit(playermirror_img,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))
    
def enemy_mirror(x,y,i):
    screen.blit(enemy_mirror_img[i],(x,y))    

def isCollision_egg(player_x,player_y,egg_x,egg_y):
    distance=math.sqrt(math.pow(player_x-egg_x,2)+math.pow(player_y-egg_y,2))
    if distance<=50:
        return True
    else:
        return False

def isCollision_nest(nest_x,nest_y,egg_x,egg_y):
    distance=math.sqrt(math.pow(nest_x-egg_x,2)+math.pow(nest_y-egg_y,2))
    if distance<=50:
        return True
    else:
        return False


def isCollision_enemy(player_x,player_y,enemy_x,enemy_y):
    distance=math.sqrt(math.pow(player_x-enemy_x,2)+math.pow(player_y-enemy_y,2))
    if distance<=50:
        return True
    else:
        return False

running=True
play=False

while running:

    

    #local variable initialisation

    #player

    player_x=250
    player_y=88
    player_globaly=88
    player_changex=0
    player_changey=0

    #egg
    
    egg_xlist=[75,150,225,500,575,650]
    egg_ylist1=[520,920]
    egg_ylist2=[320,720]
    num_of_eggs=7

    egg_img=[]
    egg_x=[]
    egg_y=[]
    egg_globaly=[]
    egg_changex=[]
    egg_changey=[]
    egg_sound=[]


    for i in range(num_of_eggs):
        egg_img.append(pygame.image.load(egg_file))
        egg_sound.append(True)
        egg_x.append(random.choice([75,150,225,500,575,650]))
                
        if egg_x[i]==75 or egg_x[i]==150 or egg_x[i]==225:
            egg_y.append(random.choice(egg_ylist1))
        elif egg_x[i]==500 or egg_x[i]==575 or egg_x[i]==650:
            egg_y.append(random.choice(egg_ylist2))
        egg_globaly.append(egg_y[i])
            

    #score
    
    score_value=num_of_eggs

    

    #clock

    time_running=False
    time_left=59
    dt = 0
    final_time=0
    t=0 # used to acquire final time


    #enemy
    enemy_file='enemy.png'
    enemy_mirror_file='enemy_mirror.png'
    enemy_img=[]
    enemy_mirror_img=[]
    enemy_x=[]
    enemy_y=[]
    enemy_globaly=[]
    enemy_changex=[]
    enemy_changey=[]
    num_of_enemies=6
    enemy_sound_track=0

    for i in range(num_of_enemies):
        
        enemy_img.append(pygame.image.load(enemy_file))
        enemy_mirror_img.append(pygame.image.load(enemy_mirror_file))
        enemy_x.append(random.randrange(0,800))
        enemy_y.append(random.randrange(300,900))
        enemy_globaly.append(enemy_y[i])
        enemy_changex.append(2)
        enemy_changey.append(2)

    screen.fill(BLACK)
    open(0,0)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            play=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                play=True   
                time_running=True
            if event.key==pygame.K_ESCAPE:
                running=False

    while play:
        screen.fill(BLACK)
        background(0,0)
        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                play=False
                running=False
                
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    print("Left key pressed")
                    player_changex=-2
                if event.key==pygame.K_RIGHT:
                    print("right key pressed")
                    player_changex=2
                if event.key==pygame.K_UP:
                    print("up key pressed")
                    player_changey=-2
                if event.key==pygame.K_DOWN:
                    print("down key pressed")
                    player_changey=2
                if event.key==pygame.K_ESCAPE or event.key==pygame.K_q:
                    play=False
                    running=False
                if event.key==pygame.K_r:
                    play=False
                    

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    print("Left key released")
                    player_changex=-2
                if event.key==pygame.K_RIGHT:
                    print("right key released")
                    player_changex=2
                if event.key==pygame.K_UP:
                    print("up key released")
                    player_changey=-2
                if event.key==pygame.K_DOWN:
                    print("down key released")
                    player_changey=2

        #to update nest image
        if player_globaly<600:
            nest_x=30
            if score_value==0:
                nest(nest_img7,nest_x,nest_y)
            elif score_value==1:
                nest(nest_img6,nest_x,nest_y)
            elif score_value==2:
                nest(nest_img5,nest_x,nest_y)
            elif score_value==3:
                nest(nest_img4,nest_x,nest_y)
            elif score_value==4:
                nest(nest_img3,nest_x,nest_y)
            elif score_value==5:
                nest(nest_img2,nest_x,nest_y)
            elif score_value==6:
                nest(nest_img1,nest_x,nest_y)
            elif score_value==7:
                nest(nest_img0,nest_x,nest_y)

        #to shift screen while moving down
        if player_globaly>600:
            background(0,-600)
            nest_x=10000
        
        
        #player movement...............................................

        #to limit play play area on left and right
        if player_x>730:
            player_changex=-2
        if player_x<0:
            player_changex=2

        #to stop player from moving up from 0 and down from 1200
        if player_globaly<=0:
            player_changey=2
        if player_globaly>=1110:
            player_changey=-2
        
        #to bounce up player from partitions 1 and 5
        if player_x<400:
            if player_globaly>=90 and player_globaly<=92:
                player_changey=-2
            if player_globaly>=890 and player_globaly<=892:
                player_changey=-2
        
        
        #to bounce up player from partitions 2 and 4
        if player_x>340:
            if player_globaly>=290 and player_globaly<=292:
                player_changey=-2
            if player_globaly>=690 and player_globaly<=692:
                player_changey=-2
            
            
        
        #to bounce up player from partition 3
        if player_x<300:
            if player_globaly>=490 and player_globaly<=492:
                player_changey=-2
            
            
        
        #to bounce down player from partitions 1 and 5
        if player_x<400:
            if player_globaly>=175 and player_globaly<=177:
                player_changey=2
            if player_globaly>=975 and player_globaly<=977:
                player_changey=2
            
            
        #to bounce down player from partitions 2 and 4. Giving range 375<y<377 leads to bug; continous motion
        if player_x>340:
            if player_globaly==376:
                player_changey=2  
            if player_globaly==776:
                player_changey=2  
        
        #to bounce down player from partition 3
        if player_x<300:
            if player_globaly>=575 and player_globaly<=577:
                player_changey=2

                
        player_x+=player_changex
        player_y+=player_changey
        player_globaly+=player_changey

        #to switch straight and mirror image to change directions
        if player_changex==2 or player_changex==0:
            player(player_x,player_y)
        elif player_changex==-2:
            player_mirror(player_x,player_y)
        
        
        # enemy movement...............................................
        for i in range(num_of_enemies):
            #to limit enemy play area on left and right
            if enemy_x[i]>730:
                enemy_changex[i]=-2
            if enemy_x[i]<0:
                enemy_changex[i]=2
            
            #to limit enemy play area on up and down
            if enemy_globaly[i]>1110:
                enemy_changey[i]=-2
            if enemy_globaly[i]<0:
                enemy_changey[i]=2
            #to restrict enemies within extra space while shifting screen
            if enemy_globaly[i]<-600:
                enemy_changey[i]=2
            if enemy_globaly[i]>1750:
                enemy_changey[i]=-2
        
        #enemy sound
        if enemy_sound_track==300:
            enemy_sound=mixer.Sound('enemy.wav')
            enemy_sound.play()
            enemy_sound_track=0
        enemy_sound_track+=1

        #to shift player, eggs and enemies while moving down and moving up. Increase the tolerance level with increase in speed.
        
        if player_globaly==600 and player_changey==2:
            player_y=0
            for i in range(num_of_enemies):
                enemy_y[i]-=600
            for i in range(num_of_eggs):
                egg_y[i]-=600
            
                
                    
        if player_globaly==598 and player_changey==-2:
            player_y=598
            for i in range(num_of_enemies):
                enemy_y[i]+=600
            for i in range(num_of_eggs):
                egg_y[i]+=600
                
                    
        
        for i in range(num_of_enemies):

            #to bounce up enemies from partitions 1 and 5. Increase the tolerance level with increase in speed.
            if enemy_x[i]<400:
                if enemy_globaly[i]>=90 and enemy_globaly[i]<=92:
                    enemy_changey[i]=-2
                if enemy_globaly[i]>=890 and enemy_globaly[i]<=892   :
                    enemy_changey[i]=-2
            #to bounce up enemies from partitions 2 and 4
            if enemy_x[i]>340:
                if enemy_globaly[i]>=290 and enemy_globaly[i]<=292:
                    enemy_changey[i]=-2
                if enemy_globaly[i]>=690 and enemy_globaly[i]<=692:
                    enemy_changey[i]=-2
            #to bounce up enemies from partition 3
            if enemy_x[i]<300:
                if enemy_globaly[i]>=490 and enemy_globaly[i]<=492:
                    enemy_changey[i]=-2
            #to bounce down enemies from partitions 1 and 5
            if enemy_x[i]<400:
                if enemy_globaly[i]>=175 and enemy_globaly[i]<=177:
                    enemy_changey[i]=2
                if enemy_globaly[i]>=975 and enemy_globaly[i]<=977:
                    enemy_changey[i]=2
            #to bounce down enemies from partitions 2 and 4
            if enemy_x[i]>340:
                if enemy_globaly[i]>=375 and enemy_globaly[i]<=377:
                    enemy_changey[i]=2
                if enemy_globaly[i]>=775 and enemy_globaly[i]<=777:
                    enemy_changey[i]=2
            #to bounce down enemies from partition 3
            if enemy_x[i]<300:
                if enemy_globaly[i]>=575 and enemy_globaly[i]<=577:
                    enemy_changey[i]=2  

        
        for i in range(num_of_enemies):
            enemy_x[i]+=enemy_changex[i]
            enemy_y[i]+=enemy_changey[i]
            enemy_globaly[i]+=enemy_changey[i]
            
            #to switch enemy images with mirrors
            if enemy_changex[i]==2:
                enemy(enemy_x[i],enemy_y[i],i)
            if enemy_changex[i]==-2:
                enemy_mirror(enemy_x[i],enemy_y[i],i)

            
            #collision with enemy
            
            collision_enemy=isCollision_enemy(player_x,player_y,enemy_x[i],enemy_y[i])
            if collision_enemy:
                death_sound=mixer.Sound('death.wav')
                death_sound.play()
                player_x=10000
                for j in range(num_of_eggs):
                    if egg_x[j]!=75 and egg_x[j]!=150 and egg_x[j]!=225 and egg_x[j]!=75 and egg_x[j]!=500 and egg_x[j]!=575 and egg_x[j]!=650: 
                        egg_x[j]=10000
                

        for i in range(num_of_eggs):        
                
            collision_egg=isCollision_egg(player_x,player_y,egg_x[i],egg_y[i])
            collision_nest=isCollision_nest(nest_x,nest_y,egg_x[i],egg_y[i])
            
            #pick up egg

            if collision_egg:
                while egg_sound[i]:
                    egg_sound[i]=mixer.Sound('egg.wav')
                    egg_sound[i].play()
                    egg_sound[i]=False
                egg_x[i]=player_x+15
                egg_y[i]=player_y

            egg(egg_x[i],egg_y[i],i)
            
            #drop egg in nest and update score

            if collision_nest:
                nest_sound=mixer.Sound('nest.wav')
                nest_sound.play()
                egg_x[i]=2000
                egg_y[i]=2000
                score_value-=1
                
                
        show_score(text_x,text_y)

        
        # conditions to end game
        
        if score_value!=0 and player_x>2000 or time_left<0.1 and not win_status :
            game_over(over_x,over_y)
            player_x=10000
            for j in range(num_of_eggs):
                if egg_x[j]!=75 and egg_x[j]!=150 and egg_x[j]!=225 and egg_x[j]!=75 and egg_x[j]!=500 and egg_x[j]!=575 and egg_x[j]!=650: 
                    egg_x[j]=10000
            time_left=0.1
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        play=False
                        
                               
        # win game

        if score_value==0:
            
            if t==0:
                final_time=round(60-time_left,2)
                final_score=round((time_left/60)*100,1)
            t+=1
            time_left=0.1
            player_x=-50000
            win_status=True
            win(win_x,win_y,final_time,final_score)
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        play=False
                        break
                        
                    if event.key==pygame.K_ESCAPE:
                        running=False
                        play=False
                        break
                    
        
        if time_running:
            time_left-=dt/1000
            dt = clock1.tick(59)
            show_clock(clock_x,clock_y)

        print('X:'+str(player_x)+ '   '+str(player_changex)+'   '+str(player_changey)+'  Y:'+str(player_y, )+'   Global Y:'+str(player_globaly)+'   Enemy X:'+str(enemy_x)+'   Enemy Y:'+str(enemy_y)+'     Egg X:'+str(egg_x)+'    Egg Y:'+str(egg_globaly))
        print(time_running)
        pygame.display.update()

    pygame.display.update()

