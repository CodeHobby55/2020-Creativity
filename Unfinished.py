import pygame
import math
from pygame.locals import *
from sys import exit
from random import *
from math import *

pygame.init()
state = 0
screen = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption("Color Clock")
font= pygame.font.SysFont("arial", 24)
colors=[(255,0,0),(0,255,0),(0,0,255)]
clock = pygame.time.Clock()

speed=500
frame_no=0
x1,x2=0,0
para=0
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


  time_passed = clock.tick(30)
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
    pygame.draw.circle(screen, (255,255,5), (320+int(i*(cos(-t1))),240+int(i*(sin((-t1))))), 5,0)
    pygame.draw.circle(screen, (5,255,255), (320+int(i*(cos(-t1+10))),240+int(i*(sin((-t1+10))))), 5,0)
    pygame.draw.circle(screen, (255,5,255), (320+int(i*(cos(-t1+20))),240+int(i*(sin((-t1+20))))), 5,0)

    pygame.draw.circle(screen, (255,0,0), (320+int(i*(cos(d1-2*pi/3))),240+int(i*(sin((d1-2*pi/3))))), 5,0)
    pygame.draw.circle(screen, (0,255,0), (320+int(i*(cos(d1))),240+int(i*(sin((d1))))), 5,0)
    pygame.draw.circle(screen, (0,0,255), (320+int(i*(cos(d1+2*pi/3))),240+int(i*(sin((d1+2*pi/3))))), 5,0)

    pygame.draw.circle(screen, (255,255,0), (320+int(i*(cos(d1-pi/3))),240+int(i*(sin((d1-pi/3))))), 5,0)
    pygame.draw.circle(screen, (0,255,255), (320+int(i*(cos(d1+pi/3))),240+int(i*(sin((d1+pi/3))))), 5,0)
    pygame.draw.circle(screen, (255,0,255), (320+int(i*(cos(d1+pi))),240+int(i*(sin((d1+pi))))), 5,0)


    pygame.draw.circle(screen, (255,255,5), (320+int(i*(cos(-t1+(i*pi/180)))),240+int(i*(sin(-t1+(i*pi/180))))), 5,0)
    pygame.draw.circle(screen, (5,255,255), (320+int(i*(cos(-t1+(2*i*pi/180)))),240+int(i*(sin(-t1+(2*i*pi/180))))), 5,0)
    pygame.draw.circle(screen, (255,5,255), (320+int(i*(cos(-t1+(3*i*pi/180)))),240+int(i*(sin(-t1+(3*i*pi/180))))), 5,0)

    pygame.draw.circle(screen, (255,5,5), (320+int(i*(cos(-t1+(4*pi/180)))),240+int(i*(sin(-t1+(i*pi/180))))), 5,0)
    pygame.draw.circle(screen, (5,255,5), (320+int(i*(cos(-t1+(5*i*pi/180)))),240+int(i*(sin(-t1+(2*i*pi/180))))), 5,0)
    pygame.draw.circle(screen, (5,5,255), (320+int(i*(cos(-t1+(6*i*pi/180)))),240+int(i*(sin(-t1+(3*i*pi/180))))), 5,0)

  sz2=2
  for i in range(20,200,5):
    pygame.draw.circle(screen, (255,255,5), (320+int(i*(cos(-t1))),240+int(i*(sin((-t1))))), sz2,0)
    pygame.draw.circle(screen, (5,255,255), (320+int(i*(cos(-t1+10))),240+int(i*(sin((-t1+10))))), sz2,0)
    pygame.draw.circle(screen, (255,5,255), (320+int(i*(cos(-t1+20))),240+int(i*(sin((-t1+20))))), sz2,0)

    pygame.draw.circle(screen, (255,0,0), (320+int(i*(cos(d1-2*pi/3))),240+int(i*(sin((d1-2*pi/3))))), sz2,0)
    pygame.draw.circle(screen, (0,255,0), (320+int(i*(cos(d1))),240+int(i*(sin((d1))))), sz2,0)
    pygame.draw.circle(screen, (0,0,255), (320+int(i*(cos(d1+2*pi/3))),240+int(i*(sin((d1+2*pi/3))))), sz2,0)

    pygame.draw.circle(screen, (255,255,0), (320+int(i*(cos(d1-pi/3))),240+int(i*(sin((d1-pi/3))))), sz2,0)
    pygame.draw.circle(screen, (0,255,255), (320+int(i*(cos(d1+pi/3))),240+int(i*(sin((d1+pi/3))))), sz2,0)
    pygame.draw.circle(screen, (255,0,255), (320+int(i*(cos(d1+pi))),240+int(i*(sin((d1+pi))))), sz2,0)


    pygame.draw.circle(screen, (255,255,5), (320+int(i*(cos(-t1+(i*pi/180)))),240+int(i*(sin(-t1+(i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, (5,255,255), (320+int(i*(cos(-t1+(2*i*pi/180)))),240+int(i*(sin(-t1+(2*i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, (255,5,255), (320+int(i*(cos(-t1+(3*i*pi/180)))),240+int(i*(sin(-t1+(3*i*pi/180))))), sz2,0)

    pygame.draw.circle(screen, (255,5,5), (320+int(i*(cos(-t1+(4*pi/180)))),240+int(i*(sin(-t1+(i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, (5,255,5), (320+int(i*(cos(-t1+(5*i*pi/180)))),240+int(i*(sin(-t1+(2*i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, (5,5,255), (320+int(i*(cos(-t1+(6*i*pi/180)))),240+int(i*(sin(-t1+(3*i*pi/180))))), sz2,0)

  sz2=2
  white=(255,255,255)
  for i in range(20,200,5):
    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1))),240+int(i*(sin((-t1))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+10))),240+int(i*(sin((-t1+10))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+20))),240+int(i*(sin((-t1+20))))), sz2,0)

    pygame.draw.circle(screen, white, (320+int(i*(cos(d1-2*pi/3))),240+int(i*(sin((d1-2*pi/3))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(d1))),240+int(i*(sin((d1))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+2*pi/3))),240+int(i*(sin((d1+2*pi/3))))), sz2,0)

    pygame.draw.circle(screen, white, (320+int(i*(cos(d1-pi/3))),240+int(i*(sin((d1-pi/3))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+pi/3))),240+int(i*(sin((d1+pi/3))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+pi))),240+int(i*(sin((d1+pi))))), sz2,0)


    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(i*pi/180)))),240+int(i*(sin(-t1+(i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(2*i*pi/180)))),240+int(i*(sin(-t1+(2*i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(3*i*pi/180)))),240+int(i*(sin(-t1+(3*i*pi/180))))), sz2,0)

    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(4*pi/180)))),240+int(i*(sin(-t1+(i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(5*i*pi/180)))),240+int(i*(sin(-t1+(2*i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(6*i*pi/180)))),240+int(i*(sin(-t1+(3*i*pi/180))))), sz2,0)


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

  sz2=1
  white=(255,127,0)
  for i in range(20,100,5):


    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+pi/6))),240+int(i*(sin((d1+pi/6))))), sz2,0)

    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+3*pi/6))),240+int(i*(sin((d1+3*pi/6))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+5*pi/6))),240+int(i*(sin((d1+5*pi/6))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+7*pi/6))),240+int(i*(sin((d1+7*pi/6))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+9*pi/6))),240+int(i*(sin((d1+9*pi/6))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(d1+12*pi/6))),240+int(i*(sin((d1+12*pi/6))))), sz2,0)

    pygame.draw.circle(screen, white, (320+int(1*i*(cos(-t1+(i*pi/180)))),240+int(i*(sin(-t1+(4*i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(1*i*(cos(-t1+(2*i*pi/180)))),240+int(i*(sin(-t1+(5*i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(1*i*(cos(-t1+(3*i*pi/180)))),240+int(i*(sin(-t1+(6*i*pi/180))))), sz2,0)

    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(4*pi/180)))),240+int(i*(sin(-t1+(i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(5*i*pi/180)))),240+int(i*(sin(-t1+(2*i*pi/180))))), sz2,0)
    pygame.draw.circle(screen, white, (320+int(i*(cos(-t1+(6*i*pi/180)))),240+int(i*(sin(-t1+(3*i*pi/180))))), sz2,0)


  
  pygame.display.update()
  
pygame.quit()
