import pygame
import sys
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
N_COLS = 10
N_ROWS = 10



def main(al_name):
    global SCREEN, CLOCK, WINDOW_HEIGHT, WINDOW_WIDTH, N_COLS, N_ROWS
    pygame.init()
    pygame.display.set_caption(al_name)
    WINDOW_HEIGHT = N_ROWS*20
    WINDOW_WIDTH = N_COLS*20
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)


    # while True:
    #     # drawGrid()
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()

    #     pygame.display.update()


def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
