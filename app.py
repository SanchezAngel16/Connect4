import pygame
import random

#GLOBAR VARS
s_width = 500
s_height = 500

BLACK = (0,0,0)
BLUE = (0,45,186)
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)

circle_radius = 30
padding = 10
value = 0
board = [[0] * 7 for i in range(8)]
win = pygame.display.set_mode((s_width, s_height))


def set_board():
    for i in range(8):
        for j in range(7):
            board[i][j] = random.randrange(0,3)

def draw_board(win):
    for i in range(8):
        for j in range(7):
            x_pos = (i*circle_radius+circle_radius + (i*circle_radius))
            y_pos = (j*circle_radius+circle_radius + (j*circle_radius) + 65)
            if board[i][j] == 0:
                pygame.draw.circle(win, BLACK, (x_pos, y_pos), circle_radius)
            elif board[i][j] == 1:
                pygame.draw.circle(win, YELLOW, (x_pos, y_pos), circle_radius)
            else:
                pygame.draw.circle(win, RED, (x_pos, y_pos), circle_radius)
                
            

def main():
    run = True
    set_board()
    while run:
        win.fill(BLUE)
        draw_board(win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.display.quit()

main()