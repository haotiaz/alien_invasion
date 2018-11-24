#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:17:38 2018

@author: apple
"""
import pygame

class Ship():
    def __init__(self,screen,settings):
        self.settings=settings
        self.screen=screen
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        self.center=self.rect.centerx
        
        self.move_left=False
        self.move_right=False
        
    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        #Update the ship's center value, checking if you can move left
        if self.move_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        #Update the rect object from self.center
        self.rect.centerx = self.center
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
