import pygame #allow us to use the module

width, height = 900, 500

win= pygame.display.set_mode((width, height))
pygame.display.set_caption('First Game')#title of the game
white= 255,255,255


def draw_window():
    win.fill((white))
    pygame.display.update()



def main():

    run =True
    while run:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
