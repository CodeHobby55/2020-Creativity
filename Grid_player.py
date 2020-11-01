import pygame
import math
from pygame.locals import *
from sys import exit
from random import *
from math import *


class dim4:
    def __init__(self, (x, y)  ):
      self.x =  x
      self.y = y
      self.rx =  5
      self.ry = 5
      
      self.atime= 0

      self.wtime= 0
      self.color = (0,255,0)
      
    def pos(self):
        return (self.x,self.y)                        

            
pygame.init()
state = 0
xsc,ysc=940,680
screen = pygame.display.set_mode((xsc,ysc), 0, 32)
pygame.display.set_caption("Color Clock")
font= pygame.font.SysFont("arial", 24)
colors=[(255,0,0),(0,255,0),(0,0,255)]
clock = pygame.time.Clock()
tick=30
speed=100
frame_no=0
x1,x2=0,0
para=0
cursor_radius = 20
cursor=1
squares=[]
oldsquares=[]

def center((px,py),(rx,ry), radius):
  if rx >= px-2*radius and rx <= px+2*radius and ry >= py-2*radius and ry <= py+2*radius:
    return 1
  else:
    return 0    

def seccenter((px,py),(rx,ry), radius):
  if (rx >= px-5*radius and rx <= px-2*radius and ry >= py-5*radius and ry <= py-2*radius) or (rx >= px-5*radius and rx <= px-2*radius and ry >= py+2*radius and ry <= py+5*radius)  or  (rx >= px+2*radius and rx <= px+5*radius and ry >= py+2*radius and ry <= py+5*radius) or  (rx >= px+2*radius and rx <= px+5*radius and ry >= py-5*radius and ry <= py-2*radius)  :
    return 1
  else:
    return 0
  
def tercenter((px,py),(rx,ry), radius):
  if (rx >= px-5*radius and rx <= px-2*radius and ry >= py-2*radius and ry <= py+2*radius) or (rx >= px-5*radius and rx <= px-2*radius and ry >= py and ry <= py+2*radius)  or  (rx >= px+2*radius and rx <= px+5*radius and ry >= py and ry <= py+2*radius) or  (rx >= px+2*radius and rx <= px+5*radius and ry >= py and ry <= py+2*radius)  :
    return 1
  else:
    return 0
  
dip=[]
for i in range(255):
  dip.append((randint(0,255) , randint(0,255)  , randint(0,255) ) )

pts=[ [(0,255,0), 320,240, 10, 5, -1,-1   ] ]

gsize=4  
grid=[]
for i in range(0,300,gsize):
  for k in range(0,600,gsize):
    grid.append((i,k))

grid2=[]
for i in range(310,600,gsize):
  for k in range(0,600,gsize):
    grid.append((i,k))

grid3=[]
for i in range(620,700,gsize):
  for k in range(100,600,gsize):
    grid.append((i,k))

singlerow= []
for data in grid:
  if data[1]<=50:
    singlerow.append(data)
        
while(state ==0):

  for event in pygame.event.get():
    if event.type == QUIT:
      state = 1
    if event.type == KEYDOWN:
      if event.key == K_q:
          screen.fill((0,0,0),Rect((0,0),(xsc,ysc)))
      if event.key == K_w:
          screen.fill((0,0,0),Rect((0,0),(xsc,ysc)))
      if event.key == K_e:
          cursor_radius+=1
      if event.key == K_r:
          if cursor_radius >= 2:
              cursor_radius-=1
          else:
              cursor_radius=1
      if event.key == K_t:
          cursor_radius+=1
      if event.key == K_y:
        dx,dy=5*gsize/6,5*gsize/6
        for data in grid:
          pygame.draw.rect(screen, (255,0,0), Rect(data,(dx,dy)))       
      if event.key == K_u:
        if cursor==1:
          cursor=0
        else:
          cursor=1
      if event.key == K_i:
        squares.append(dim4(pygame.mouse.get_pos()) )  




##  for i in range(20,200,15):
##    pygame.draw.circle(screen, dip[0], (cts[0][0]+int(rad[0]*(cos(-t1))),cts[0][1]+int(rad[1]*(sin((-t1))))), 5,0)

##pts=[ [color0, xcent1, ycent2, orbitrad3,  satrad4,  periodx5,  periody6   ] ]
  
##  screen.fill((0,0,0),Rect((0,0),(640,40)))
##  screen.fill((0,0,0),Rect((0,0),(40,480)))
##  screen.fill((0,0,0),Rect((0,440),(640,480)))
##  screen.fill((0,0,0),Rect((600,440),(640,480)))
  if cursor==1:
    pygame.draw.circle(screen, (0,0,255), pygame.mouse.get_pos(),cursor_radius,1 )
    
  if len(squares)!=0:
    for data in squares:
      if data.atime<=0.3:
        pygame.draw.rect(screen, (0,0,255), Rect(data.x,data.y,data.rx,data.ry))
      else:
        pygame.draw.rect(screen, data.color, Rect(data.x,data.y,data.rx,data.ry))
        pygame.draw.rect(screen, data.color, Rect(data.x+data.rx,data.y-data.ry,data.rx,data.ry))
        pygame.draw.rect(screen, data.color, Rect(data.x-data.rx,data.y+data.ry,data.rx,data.ry))
        
  for data in squares:
      if data.atime>0.4:
          squares.append(dim4((data.x-data.rx,data.y-data.ry)))

          squares.remove(data)
          oldsquares.append(data)
  print len(squares)
          
 
  time_passed = clock.tick(30)
  time_seconds=time_passed/1000.0
  for data in squares:
    data.atime+=time_seconds
 
        
  pygame.display.update()
  
pygame.quit()
