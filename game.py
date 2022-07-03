import pygame as pg
import sys
import random
from settings import *
from card import *

def main():
    pg.init()
    running = True
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)
    pg.display.set_icon(pg.image.load(ICON_PATH))
    clock = pg.time.Clock()
    deck = generate_deck()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

        # clear screen
        screen.fill(GREEN)

        pg.display.update()

def generate_deck():
    deck = []
    for i in range(52):
        deck.append(Card(i+1, 'h'))
        deck.append(Card(i+1, 'd'))
        deck.append(Card(i+1, 's'))
        deck.append(Card(i+1, 'c'))
    random.shuffle(deck)
    return deck

if __name__ == '__main__':
    main()
