import pygame
import random
import time
from pygame.locals import *
import random


pygame.init()


s=[1,-1]
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

white=(255,255,255)
width=1280
height=768

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Pong Game')
font=pygame.font.SysFont(None,25)

tiles={}


tiles[4] = pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Tiles/Tile (1).png")

tiles[5] = pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Tiles/Tile (2).png")

tiles[1] = pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Tiles/Tile (14).png")

tiles[2]= pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Tiles/Tile (15).png")

tiles[3] = pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Tiles/Tile (16).png")



bgsize =pygame.image.load( 'C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/BG.png')

bg =pygame.transform.scale(bgsize,(width,height))


tiles['tr']= pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Objects/Tree.png")
tiles['bl']= pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Objects/Bush (1).png")
tiles['b2'] = pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Objects/Bush (2).png")
tiles['Ab']= pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Objects/ArrowSign.png")
tiles['cr']= pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Objects/Crate.png")
tiles['bx']= pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Objects/SIgn.png")
tiles['sk'] = pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Objects/Skeleton.png")
tiles['t1'] = pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Objects/TombStone (1).png") 
tiles['t2'] = pygame.image.load("C:/Users/youngwonks/Downloads/graveyardtilesetnew(1)/png/Objects/TombStone (2).png")



run=[]

for i in range(10):
    r = pygame.image.load('C:/Users/youngwonks/Downloads/ninjaadventurenew (1)/png/Run__00'+str(i)+'.png')
    size_r=pygame.transform.scale(r,(128,128))
    run.append(size_r)

left_run=[]

for i in range(10):
    r = pygame.image.load('C:/Users/youngwonks/Downloads/ninjaadventurenew (1)/png/Run__00'+str(i)+'.png')
    size_r=pygame.transform.scale(r,(128,128))
    flip_r=pygame.transform.flip(size_r,True,False)
    left_run.append(flip_r)


idle=[]
for i in range(10):
    a = pygame.image.load('C:/Users/youngwonks/Downloads/ninjaadventurenew (1)/png/Idle__00'+str(i)+'.png')
    size_i=pygame.transform.scale(a,(128,128))
    idle.append(size_i)

frame=len(idle)
print(frame)
left_idle=[]
for i in range(10):
    a = pygame.image.load('C:/Users/youngwonks/Downloads/ninjaadventurenew (1)/png/Idle__00'+str(i)+'.png')
    size_i=pygame.transform.scale(a,(128,128))
    flip_i=pygame.transform.flip(size_i,True,False)
    left_idle.append(flip_i)


jump=[]
for i in range(10):
    j = pygame.image.load('C:/Users/youngwonks/Downloads/ninjaadventurenew (1)/png/Jump_Throw__00'+str(i)+'.png')
    size_j=pygame.transform.scale(j,(128,128))
    jump.append(size_j)


left_jump=[]
for i in range(10):
    j = pygame.image.load('C:/Users/youngwonks/Downloads/ninjaadventurenew (1)/png/Jump_Attack__00'+str(i)+'.png')
    size_j=pygame.transform.scale(j,(128,128))
    flip_j=pygame.transform.flip(size_j,True,False)
    left_jump.append(flip_j)


coin_img = pygame.image.load('C:/Users/youngwonks/Downloads/coin.jpg')
coin_img=pygame.transform.scale(coin_img,(64,64))


i=0
x =128
y= 0


def right_running():
    global i,x,y    
    screen.blit(run[i], (x,y))
    i+=1
    if i>=10:
        i=0
  

def left_running():
    global i  , x,y     
    screen.blit(left_run[i], (x,y))
    i+=1
    if i>=10:
        i=0



def idling():
    global i, x,y    
    screen.blit(idle[i], (x, y))
    i+=1
    if i>=frame:
        i=0
  

def left_idling():
    global i ,x,y   
    screen.blit(left_idle[i], (x,y))
    i+=1
    if i>=10:
        i=0


def jumping():
    global i    
    screen.blit(jump[i], (x,y))
    i+=1
    if i>=10:
        i=0
  

def left_jumping():
    global i    
    screen.blit(left_jump[i], (x,y))
    i+=1
    if i>=10:
        i=0

 

Level_1=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 2, 3, 4],
         [0, 0, 0, 0, 2, 4, 0, 0, 0, 0],
         [0, 2, 4, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 4, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

Level_3=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 'bx'],
         [0, 0, 0, 0, 0, 'tr', 0, 1, 2, 3],
         [0, 't2', 0, 0, 1, 3, 0, 0, 0, 0],
         [0, 1, 3, 0, 0, 'sk', 0, 0, 0, 0],
         ['Ab', 0, 0, 0, 1, 3, 0, 0, 0, 0],
         [4, 5, 0, 0, 0, 0, 0, 0, 0, 0]]

objects=['tr', 'bl', 'b2', 'Ab', 'c', 'bx', 'sk', 't1', 't2']
def tile(level):
    for i, row in enumerate (level):
        for j,column in enumerate(row):
            if column != 0:
                screen.blit(tiles [column], (j*128, i*128))


def draw_level (level):
    for i, row in enumerate (level):
        for j,column in enumerate(row):
            if column!=0:
                if column in objects:
                    h=tiles[column].get_height()
                    w=tiles[column].get_width()
                    adjusted_y=0
                    adjusted_x=0
                    
                    if w>128:
                        adjusted_x=128-w
                        
                    if h>128 or h<128:
                        adjusted_y=128-h
                        
                    screen.blit(tiles [column], (j*128+adjusted_x, i*128+adjusted_y+1))
                else:
                    screen.blit(tiles [column], (j*128,i*128))


collidables= [1,2,3,4,5]
rects=[]


def get_rects(level):
    for i,row in enumerate(level):
        for j,column in enumerate (row):
            if column in collidables:
                rect=pygame.Rect(j*128, i*128, 128,128)
                if rect not in rects:
                    rects.append(rect)




coin_postions_1v13=[[2,2],[4,1],[0,8],[3,4],[1,5]]

##for row in coin_positions_lvl3:
##    for column in row:
##        print(column)

coin_objs=[]
def draw_coins (row,col):
    global coin_objs
    coin=screen.blit(coin_img, (col*128+32, row*128+32))
    if coin not in coin_objs:
        coin_objs.append(coin)

def display_coins(positions):
    for i,row in enumerate(positions):
        
        draw_coins(row[0], row[1])


def grid():
    for i in range(0,1280,128):
        pygame.draw.line(screen,'gray',(i,0), (i,height),1)

    for i in range(0,1280,128):
        pygame.draw.line(screen,'gray',(0,i), (width,i),1)
flipped = False
runaction = False

jumpup=False
ground= True

movex=0

pygame.key.set_repeat(1,1)
while 1:

    screen.blit(bg,(0,0))
    
    draw_level (Level_3)
    get_rects(Level_3)

    display_coins(coin_postions_1v13)
    if runaction and flipped :
        left_running()
    if runaction and not flipped :
        right_running()
    if not runaction and not flipped :
        jumping()
    if not runaction and flipped:
        left_jumping()

    y += 5

    pygame.display.update()
    if flipped:
        if ground:
            player = screen.blit(left_idle[frame//2],(x,y))
        if ground and runaction:
            player = screen.blit(left_run[frame//2],(x,y))
        if jumpup:
            player = screen.blit(left_jump[frame//2],(x,y))
        if not jumpup and not ground:
            player = screen.blit(left_jump[-1],(x,y))
    if not flipped:
        if ground:
            player = screen.blit(idle[frame//2],(x,y))
        if ground and runaction:
            player = screen.blit(run[frame//2],(x,y))
        if jumpup:
            player = screen.blit(jump[frame//2],(x,y))
        if not jumpup and not ground:
            player = screen.blit(jump[-1],(x,y))
    hits = player.collidelistall(rects)

    for j in hits:
        if rects[j].collidepoint(player.midbottom):
            y = rects[j].top- player.height+1
            ground = True
            break
        else:
            ground= False

    cointouch=player.collidelistall (coin_objs)
    if len(cointouch)!=0:
        coin_postions_1v13.pop(cointouch[0])
        coin_objs.pop (cointouch [0])
        cointouch.pop()
        
    x += movex
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN: 
            if event.key ==pygame.K_SPACE:
                y =y-1
                #jumpup= True
                runaction=False
                
            if event.key ==pygame.K_LEFT:
                runaction=True
                flipped = True
                #jumpup= False
                movex=-10
                 
            elif event.key == pygame.K_RIGHT:
                runaction=True
                flipped = False
                #jumpup= False
                movex=10
                
        if event.type == pygame.KEYUP: #
            #jumpup= False
            if event.key == pygame.K_SPACE:
                ground = False
                #jumpup= False
              
            if event.key ==pygame.K_LEFT:
                runaction = False
                movex=0
                
                
            if event.key == pygame.K_RIGHT:
                runaction = False
                movex=0
                
