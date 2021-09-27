#allow us to use the module

import pygame
import os

width, height = 900, 500

win= pygame.display.set_mode((width, height))
pygame.display.set_caption('First Game')#title of the game
white= 255,255,255

fps= 60
vel = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40



YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90) #changes the image size and its position





RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270) #changes the image size



def draw_window(red, yellow):
    win.fill((white))
    win.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))#add to the screen
    win.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()



def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)




    
    clock = pygame.time.Clock()
    run =True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: # left key
            yellow.x -= vel


        draw_window(red, yellow)

    pygame.quit()


if __name__ == '__main__':
    main()
