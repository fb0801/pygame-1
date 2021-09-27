import pygame #allow us to use the module

width, height = 900, 500

win= pygame.display.set_mode((width, height))


def main():

    run =True
    while run:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False

    pygame.quit()
