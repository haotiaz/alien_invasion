#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:35:07 2018

@author: apple
"""

import pygame
import sys

def check_events(screen,settings,ship):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYUP:
            check_keyup_event(event,screen,settings,ship)
        if event.type==pygame.KEYDOWN:
            check_keydown_event(event,screen,settings,ship)
            
def check_keyup_event(event,screen,settings,ship):
    if event.key==pygame.K_RIGHT:
        ship.move_right=True
    if event.key==pygame.K_LEFT:
        ship.move_left=True
        
def check_keydown_event(event,screen,settings,ship):
    if event.key==pygame.K_RIGHT:
        ship.move_right=False
    if event.key==pygame.K_LEFT:
        ship.move_left=False
        
def update_screen(screen,settings,ship):
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()
    
        