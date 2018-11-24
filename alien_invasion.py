#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:56:06 2018

@author: apple
"""
from settings import Settings
import pygame
from ship import Ship
import game_logic as gl
import sys

def run_game():
    pygame.init()
    settings=Settings()
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    ship=Ship(screen,settings)
    
    while True:
       gl.check_events(screen,settings,ship)
       ship.update()
       gl.update_screen(screen,settings,ship)
run_game()