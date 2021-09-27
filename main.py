#allow us to use the module

import pygame
import os

width, height = 900, 500

win= pygame.display.set_mode((width, height))
pygame.display.set_caption('First Game')#title of the game
white= 255,255,255

fps= 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40



YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.image.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90) #changes the image size





RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)) #changes the image size



def draw_window():
    win.fill((white))
    win.blit(YELLOW_SPACESHIP, (300, 100))#add to the screen
    pygame.display.update()



def main():
    clock = pygame.time.Clock()
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
