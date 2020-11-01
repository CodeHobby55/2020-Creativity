import pygame
import math
from pygame.locals import *
from sys import exit
from random import *
from math import *

pygame.init()
state = 0
xsc,ysc=940,680
screen = pygame.display.set_mode((xsc,ysc), 0, 32)
pygame.display.set_caption("Color Clock")
font= pygame.font.SysFont("arial", 24)
colors=[(255,0,0),(0,255,0),(0,0,255)]
clock = pygame.time.Clock()
tick=30
speed=500
frame_no=0
x1,x2=0,0
para=0


cts=[[320,240]]
for i in range(50):
  cts.append([320,240])

rad=[]
for i in range(100):
  rad.append(randint(1,10))


dip=[]
for i in range(255):
  dip.append((randint(0,255) , randint(0,255)  , randint(0,255) ) )


  

while(state ==0):
  screen.fill((0,0,0),Rect((0,0),(640,480)))
  for event in pygame.event.get():
    if event.type == QUIT:
      state = 1
    if event.type == KEYDOWN:
      if event.key == K_q:
          state = 1
      if event.key == K_w:
          pygame.draw.circle(screen, (5,255,5), pygame.mouse.get_pos(), 10,0)
      if event.key == K_e:
        if (para ==0): 
          para=1
        elif (para ==1):
          para=0
      if event.key == K_r:
        tick-=5
      if event.key == K_t:
        tick+=5
      if event.key == K_y:
        for data in cts:
          data[0]=randint(0,640)
          data[1]=randint(0,480)

      if event.key == K_b:
        cts=[]
        for i in range(50):
          cts.append([320,240])       

      if event.key == K_h:
        for data in cts:
          data[0]+=randint(5,20)
          data[1]+=randint(5,20)


      if event.key == K_u:
        for data in cts:
          data[0]=320
          data[1]=240

      if event.key == K_j:
        rad=[]
        for i in range(100):
          rad.append(1)
  

      if event.key == K_i:
        rad=[]
        for i in range(100):
          rad.append(randint(2,50))
     
        
  time_passed = clock.tick(tick)
  time_seconds=time_passed/1000.0  
  distance_moved=time_seconds*speed
          
  if (para ==1): 
    x1+= distance_moved
  elif (para ==0):
    x1-= distance_moved
    

  t1=x1/speed
  d1=(t1)
  
  if abs(degrees(t1)) >= 359 and  abs(degrees(t1)) <= 360:
    t1=0
  for i in range(20,200,15):
    pygame.draw.circle(screen, dip[0], (cts[0][0]+int(rad[0]*(cos(-t1))),cts[0][1]+int(rad[1]*(sin((-t1))))), 5,0)
    pygame.draw.circle(screen, dip[1], (cts[1][0]+int(rad[2]*(cos(-t1+10))),cts[1][1]+int(rad[3]*(sin((-t1+10))))), 5,0)
    pygame.draw.circle(screen, dip[2], (cts[2][0]+int(rad[4]*(cos(-t1+20))),cts[2][1]+int(rad[5]*(sin((-t1+20))))), 5,0)

    pygame.draw.circle(screen, dip[3], (cts[3][0]+int(rad[6]*(cos(d1-2*pi/3))),cts[3][1]+int(rad[9]*(sin((d1-2*pi/3))))), 5,0)
    pygame.draw.circle(screen, dip[4], (cts[4][0]+int(rad[7]*(cos(d1))),cts[4][1]+int(rad[10]*(sin((d1))))), 5,0)
    pygame.draw.circle(screen, dip[5], (cts[5][0]+int(rad[8]*(cos(d1+2*pi/3))),cts[5][1]+int(rad[11]*(sin((d1+2*pi/3))))), 5,0)

    pygame.draw.circle(screen, dip[6], (cts[6][0]+int(rad[12]*(cos(d1-pi/3))),cts[6][1]+int(rad[15]*(sin((d1-pi/3))))), 5,0)
    pygame.draw.circle(screen, dip[7], (cts[7][0]+int(rad[13]*(cos(d1+pi/3))),cts[7][1]+int(rad[16]*(sin((d1+pi/3))))), 5,0)
    pygame.draw.circle(screen, dip[8], (cts[8][0]+int(rad[14]*(cos(d1+pi))),cts[8][1]+int(rad[17]*(sin((d1+pi))))), 5,0)


    pygame.draw.circle(screen, dip[9], (cts[9][0]+int(rad[18]*(cos(-t1+(i*pi/180)))),cts[9][1]+int(rad[19]*(sin(-t1+(i*pi/180))))), 5,0)
    pygame.draw.circle(screen, dip[10], (cts[10][0]+int(rad[20]*(cos(-t1+(2*i*pi/180)))),cts[10][1]+int(rad[21]*(sin(-t1+(2*i*pi/180))))), 5,0)
    pygame.draw.circle(screen, dip[11], (cts[11][0]+int(rad[22]*(cos(-t1+(3*i*pi/180)))),cts[11][1]+int(rad[23]*(sin(-t1+(3*i*pi/180))))), 5,0)

    pygame.draw.circle(screen, dip[12], (cts[12][0]+int(i*(cos(-t1+(rad[24]*pi/180)))),cts[12][1]+int(rad[25]*(sin(-t1+(i*pi/180))))), 5,0)
    pygame.draw.circle(screen, dip[13], (cts[13][0]+int(i*(cos(-t1+(rad[26]*i*pi/180)))),cts[13][1]+int(rad[27]*(sin(-t1+(2*i*pi/180))))), 5,0)
    pygame.draw.circle(screen, dip[14], (cts[14][0]+int(i*(cos(-t1+(rad[28]*i*pi/180)))),cts[14][1]+int(rad[29]*(sin(-t1+(3*i*pi/180))))), 5,0)

  sz2=2
  for i in range(20,200,5):
    pygame.draw.circle(screen, dip[15], (cts[15][0]+int(rad[randint(0,45)]*(cos(-t1))),cts[15][1]+int(rad[randint(0,50)]*(sin((-t1))))), sz2,0)
    pygame.draw.circle(screen, dip[16], (cts[16][0]+int(rad[randint(0,45)]*(cos(-t1+10))),cts[16][1]+int(rad[randint(0,50)]*(sin((-t1+10))))), sz2,0)
    pygame.draw.circle(screen, dip[17], (cts[17][0]+int(rad[randint(0,45)]*(cos(-t1+20))),cts[17][1]+int(rad[randint(0,50)]*(sin((-t1+20))))), sz2,0)

    pygame.draw.circle(screen, dip[18], (cts[18][0]+int(rad[randint(0,45)]*(cos(d1-2*pi/3))),cts[18][1]+int(rad[randint(0,50)]*(sin((d1-2*pi/3))))), sz2,0)
    pygame.draw.circle(screen, dip[19], (cts[19][0]+int(rad[randint(0,45)]*(cos(d1))),cts[19][1]+int(rad[randint(0,50)]*(sin((d1))))), sz2,0)
    pygame.draw.circle(screen, dip[20], (cts[20][0]+int(rad[randint(0,45)]*(cos(d1+2*pi/3))),cts[20][1]+int(rad[randint(0,50)]*(sin((d1+2*pi/3))))), sz2,0)

    pygame.draw.circle(screen, dip[20], (cts[21][0]+int(rad[randint(0,45)]*(cos(d1-pi/3))),cts[21][1]+int(rad[randint(0,50)]*(sin((d1-pi/3))))), sz2,0)
    pygame.draw.circle(screen, dip[21], (cts[22][0]+int(rad[randint(0,45)]*(cos(d1+pi/3))),cts[22][1]+int(rad[randint(0,50)]*(sin((d1+pi/3))))), sz2,0)
    pygame.draw.circle(screen, dip[22], (cts[23][0]+int(rad[randint(0,45)]*(cos(d1+pi))),cts[23][1]+int(rad[randint(0,50)]*(sin((d1+pi))))), sz2,0)


    pygame.draw.circle(screen, dip[23], (cts[24][0]+int(rad[randint(10,15)]*(cos(-t1+(i*pi/180)))),cts[24][1]+int(rad[randint(20,50)]*(sin(-t1+(i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, dip[24], (cts[25][0]+int(rad[randint(0,5)]*(cos(-t1+(2*i*pi/180)))),cts[25][1]+int(rad[randint(30,50)]*(sin(-t1+(2*i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, dip[25], (cts[26][0]+int(rad[randint(0,25)]*(cos(-t1+(3*i*pi/180)))),cts[26][1]+int(rad[randint(40,50)]*(sin(-t1+(3*i*pi/180))))), sz2,0)

##    pygame.draw.circle(screen, (255,5,5), (cts[27][0]+int(rad[0]*(cos(-t1+(4*pi/180)))),cts[27][1]+int(rad[0]*(sin(-t1+(i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, (5,255,5), (cts[28][0]+int(rad[0]*(cos(-t1+(5*i*pi/180)))),cts[28][1]+int(rad[0]*(sin(-t1+(2*i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, (5,5,255), (cts[29][0]+int(rad[0]*(cos(-t1+(6*i*pi/180)))),cts[29][1]+int(rad[0]*(sin(-t1+(3*i*pi/180))))), sz2,0)

##  sz2=2
##  white=(255,255,255)
##  for i in range(20,200,5):
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1))),240+int(i*(sin((-t1))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+10))),240+int(i*(sin((-t1+10))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+20))),240+int(i*(sin((-t1+20))))), sz2,0)
##
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1-2*pi/3))),240+int(i*(sin((d1-2*pi/3))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1))),240+int(i*(sin((d1))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+2*pi/3))),240+int(i*(sin((d1+2*pi/3))))), sz2,0)
##
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1-pi/3))),240+int(i*(sin((d1-pi/3))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+pi/3))),240+int(i*(sin((d1+pi/3))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+pi))),240+int(i*(sin((d1+pi))))), sz2,0)
##
##
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(i*pi/180)))),240+int(i*(sin(-t1+(i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(2*i*pi/180)))),240+int(i*(sin(-t1+(2*i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(3*i*pi/180)))),240+int(i*(sin(-t1+(3*i*pi/180))))), sz2,0)
##
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(4*pi/180)))),240+int(i*(sin(-t1+(i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(5*i*pi/180)))),240+int(i*(sin(-t1+(2*i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(6*i*pi/180)))),240+int(i*(sin(-t1+(3*i*pi/180))))), sz2,0)


##  sz2=2
##  white=(255,255,255)
##  for i in range(20,200,5):
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1))),240+int(i*(sin((-t1))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+10))),240+int(i*(sin((-t1+10))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+20))),240+int(i*(sin((-t1+20))))), sz2,0)
##
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1-2*pi/3))),240+int(i*(sin((d1-2*pi/3))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1))),240+int(i*(sin((d1))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+2*pi/3))),240+int(i*(sin((d1+2*pi/3))))), sz2,0)
##
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1-pi/3))),240+int(i*(sin((d1-pi/3))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+pi/3))),240+int(i*(sin((d1+pi/3))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+pi))),240+int(i*(sin((d1+pi))))), sz2,0)
##
##
##    pygame.draw.circle(screen, white, (320+int(1*i*(cos(-t1+(i*pi/180)))),240+int(i*(sin(-t1+(4*i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(1*i*(cos(-t1+(2*i*pi/180)))),240+int(i*(sin(-t1+(5*i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(1*i*(cos(-t1+(3*i*pi/180)))),240+int(i*(sin(-t1+(6*i*pi/180))))), sz2,0)
##
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(4*pi/180)))),240+int(i*(sin(-t1+(i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(5*i*pi/180)))),240+int(i*(sin(-t1+(2*i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(6*i*pi/180)))),240+int(i*(sin(-t1+(3*i*pi/180))))), sz2,0)

##  sz2=1
##  white=(255,127,0)
##  for i in range(20,100,5):
##
##
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+pi/6))),240+int(i*(sin((d1+pi/6))))), sz2,0)
##
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+3*pi/6))),240+int(i*(sin((d1+3*pi/6))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+5*pi/6))),240+int(i*(sin((d1+5*pi/6))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+7*pi/6))),240+int(i*(sin((d1+7*pi/6))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+9*pi/6))),240+int(i*(sin((d1+9*pi/6))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+12*pi/6))),240+int(i*(sin((d1+12*pi/6))))), sz2,0)
##
##    pygame.draw.circle(screen, white, (320+int(1*i*(cos(-t1+(i*pi/180)))),240+int(i*(sin(-t1+(4*i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(1*i*(cos(-t1+(2*i*pi/180)))),240+int(i*(sin(-t1+(5*i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(1*i*(cos(-t1+(3*i*pi/180)))),240+int(i*(sin(-t1+(6*i*pi/180))))), sz2,0)
##
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(4*pi/180)))),240+int(i*(sin(-t1+(i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(5*i*pi/180)))),240+int(i*(sin(-t1+(2*i*pi/180))))), sz2,0)
##    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(6*i*pi/180)))),240+int(i*(sin(-t1+(3*i*pi/180))))), sz2,0)


  
  pygame.display.update()
  
pygame.quit()
