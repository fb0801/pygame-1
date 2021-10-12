#allow us to use the module

import pygame
import os

width, height = 900, 500

win= pygame.display.set_mode((width, height))
pygame.display.set_caption('First Game')#title of the game

white= (255,255,255)
black = (0,0,0)
red=(255,0,0)
yellow= (255,255)

BORDER = pygame.Rect(width//2 - 5,0,10,height)


fps= 60
vel = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

BULLET_VEL = 7
MAX_BULLETS= 3

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90) #changes the image size and its position


YELLOW_HIT = pygame.USEREVENT +1
RED_HIT = pygame.USEREVENT +2


RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270) #changes the image size
SPACE= pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')), (width,height))


def draw_window(red, yellow, red_bullets, yellow_bullets):
    win.fill(white)
    pygame.draw.rect(win, black, BORDER)
    win.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))#add to the screen
    win.blit(RED_SPACESHIP, (red.x, red.y))


    for bullet in red_bullets:
        pygame.draw.rect(win, red, bullet)


    for bullet in yellow_bullets:
        pygame.draw.rect(win, yellow, bullet)

        
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
    #take key pressed and red character
     if keys_pressed[pygame.K_LEFT] and red.x - vel > BORDER.x + BORDER.width: # left key
         red.x -= vel
     if keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < width: # right key
         red.x += vel
     if keys_pressed[pygame.K_UP] and red.y - vel > 0: # up key
         red.y -= vel
     if keys_pressed[pygame.K_DOWN] and red.y + vel + red.height < height - 15: # dwn key
         red.y += vel

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    #handle the game characters to shoot
    for bullet in yellow_bullets:
        bullet.x +=BULLET_VEL
        if red.colliderect(bullet):
            #tell us if collison happen
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

        elif bullet.x > width:
            yellow_bullets.remove(bullet)
            
    for bullet in red_bullets:
        bullet.x -=BULLET_VEL
        if yellow.colliderect(bullet):
            #tell us if collison happen
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def main():
    #run the game 
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)


    red_bullets =[]
    yellow_bullets= []
    
    clock = pygame.time.Clock()
    run =True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet=pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10,5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet=pygame.Rect(red.x, red.y + red.height//2 - 2, 10,5)
                    red_bullets.append(bullet)

            
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)


        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        
        draw_window(red, yellow, red_bullets, yellow_bullets)

    pygame.quit()


if __name__ == '__main__':
    main()
