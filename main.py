#allow us to use the module

import pygame
import os

width, height = 900, 500

win= pygame.display.set_mode((width, height))
pygame.display.set_caption('First Game')#title of the game
white= (255,255,255)
black = (0,0,0)
BORDER = pygame.Rect(width/2 - 5,0,10,height)


fps= 60
vel = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40



YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90) #changes the image size and its position





RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270) #changes the image size



def draw_window(red, yellow):
    win.fill(white)
    pygame.draw.rect(win, black, BORDER)
    win.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))#add to the screen
    win.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    #take key pressed and yellow character
     if keys_pressed[pygame.K_a] and yellow.x - vel > 0: # left key
         yellow.x -= vel
     if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < BORDER.x: # right key
         yellow.x += vel
     if keys_pressed[pygame.K_w] and yellow.y - vel > 0: # up key
         yellow.y -= vel
     if keys_pressed[pygame.K_s]and yellow.y + vel + yellow.height < height - 15: # dwn key
         yellow.y += vel


def red_handle_movement(keys_pressed, red):
    #take key pressed and yellow character
     if keys_pressed[pygame.K_LEFT] and red.x - vel > BORDER.x + BORDER.width: # left key
         red.x -= vel
     if keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < width: # right key
         red.x += vel
     if keys_pressed[pygame.K_UP] and red.y - vel > 0: # up key
         red.y -= vel
     if keys_pressed[pygame.K_DOWN] and red.y + vel + red.height < height - 15: # dwn key
         red.y += vel

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
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()


if __name__ == '__main__':
    main()
