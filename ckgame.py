import sys, pygame, random
import os
#from ck import *
pygame.init()

# set colour and size of screen
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 600
GRID_WIDTH = 100
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red n' Black")

# set refresh rate
FPS = 30
clock = pygame.time.Clock()

# add background image
base_folder = os.path.dirname(__file__)
img_folder = os.path.join(base_folder, 'images')
background_img = pygame.image.load(os.path.join(img_folder, 'board.png')).convert()
background_img_2 = pygame.image.load(os.path.join(img_folder, 'wood.jpg')).convert()

# draw the board (8 * 8)
def draw_background(surf):
    # load background image
    surf.blit(background_img_2, (0, 0))
    surf.blit(background_img, (100, 100))

    # draw board rim
    # print ((GRID_WIDTH, GRID_WIDTH))
    rect_lines = [
        ((GRID_WIDTH, GRID_WIDTH), (GRID_WIDTH, HEIGHT - GRID_WIDTH)),
        ((GRID_WIDTH, GRID_WIDTH), (WIDTH - GRID_WIDTH, GRID_WIDTH)),
        ((GRID_WIDTH, HEIGHT - GRID_WIDTH),
            (WIDTH - GRID_WIDTH, HEIGHT - GRID_WIDTH)),
        ((WIDTH - GRID_WIDTH, GRID_WIDTH),
            (WIDTH - GRID_WIDTH, HEIGHT - GRID_WIDTH)),
    ]
    for line in rect_lines:
        pygame.draw.line(surf, BLACK, line[0], line[1], 2)

    # draw grid
    for i in range(1, 8):
        count = (50 * i) + 100
        # print ((GRID_WIDTH * count, GRID_WIDTH))
        
        pygame.draw.line(surf, BLACK,
                         (count, GRID_WIDTH),
                         (count, HEIGHT - GRID_WIDTH))
        pygame.draw.line(surf, BLACK,
                         (GRID_WIDTH, count),
                         (HEIGHT - GRID_WIDTH, count))
        '''
        pygame.draw.line(surf, BLACK,
                         (150, 100),
                         (150, 500))
        '''

running = True
while running:
    # set refresh
    clock.tick(FPS)

    for event in pygame.event.get():
        # check if windows is quit
        if event.type == pygame.QUIT:
            running = False

    # draw the background board
    draw_background(screen)

    # refresh
    pygame.display.flip()
