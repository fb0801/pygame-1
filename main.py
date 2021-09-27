#allow us to use the module

import pygame
import os

width, height = 900, 500

win= pygame.display.set_mode((width, height))
pygame.display.set_caption('First Game')#title of the game
white= 255,255,255

fps= 60
yellow_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
red_spaceship_image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

def draw_window():
    win.fill((white))
    pygame.display.update()



def main():
    clock = pygame.time.clock()
    run =True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
