from settings import *
import pygame as pg

class Card(pg.sprite.Sprite):

    def __init__(self, rank, suit, image): # maybe pass sprite image at construction will allow for collision detection?
        super().__init__()
        self.rank = rank #  1-13
        self.suit = suit #  h, d, s, c 
        self.color = 'r'
        
        if self.suit == 's' or self.suit == 'c':
            self.color = 'b'

        #  sprite coordinates
        suits = {'h' : CARD_HEIGHT * 2, 'd' : CARD_HEIGHT * 3, 's' : CARD_HEIGHT, 'c' : 0}
        self.y = suits[suit]
        self.x = (rank - 1) * CARD_WIDTH

        spritesheet = Spritesheet(FILENAME)
        self.image = spritesheet.get_sprite(self.x, self.y, CARD_WIDTH, CARD_HEIGHT)

        self.rect = self.image.get_rect()

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.spritesheet = pg.image.load(filename).convert()

    def get_sprite(self, x, y, w, h):
        sprite = pg.Surface((w, h))
        sprite.blit(self.spritesheet, (0, 0), (x, y, w, h))
        return sprite
