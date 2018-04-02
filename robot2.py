import RPi.GPIO as gpio
import pygame
import time
import sys

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7,gpio.OUT)
    gpio.setup(11,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.OUT)

def forward(tf):
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    init()
    gpio.output(7,True)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    init()
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()

pygame.init()
size = (300,400)
pygame.display.set_mode(size)
pygame.display.set_caption("CAR")
carryOn = True

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        forward(0.5)
    if keys[pygame.K_DOWN]:
        reverse(0.5)
    if keys[pygame.K_LEFT]:
        turn_left(0.5)
    if keys[pygame.K_RIGHT]:
        turn_right(0.5)
    if keys[pygame.K_p]:
        pivot_left(0.5)
    if keys[pygame.K_q]:
        pivot_right(0.5)

pygame.quit()
#forward(1)
#reverse(1)
#turn_left(1)
#turn_right(1)
#pivot_left(1)
#pivot_right(1)

