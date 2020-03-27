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
player_pos = 1

def draw_board(win):
    for i in range(8):
        for j in range(7):
            x_pos = (i*circle_radius+circle_radius + (i*circle_radius) + 10)
            y_pos = (j*circle_radius+circle_radius + (j*circle_radius) + 75)
            if board[i][j] == 0:
                pygame.draw.circle(win, BLACK, (x_pos, y_pos), circle_radius)
            elif board[i][j] == 1:
                pygame.draw.circle(win, YELLOW, (x_pos, y_pos), circle_radius)
            else:
                pygame.draw.circle(win, RED, (x_pos, y_pos), circle_radius)
                
def insert_on_board(pos_x, turn):
    insertion = 0
    for i in range(7):
        if board[pos_x][i] == 0:
            insertion = i
    board[pos_x][insertion] = turn

def main():
    run = True
    player_pos = 0
    turn = 1
    while run:
        win.fill(BLUE, (0,70,s_width,s_height))
        win.fill(BLACK, (0,0, s_width, 70))
        draw_board(win)
        if turn == 1:
            pygame.draw.circle(win, YELLOW, (40 + (player_pos*60),35), circle_radius)
        else:
            pygame.draw.circle(win, RED, (40 + (player_pos*60),35), circle_radius)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and player_pos < 7:
                    player_pos += 1
                if event.key == pygame.K_LEFT and player_pos > 0:
                    player_pos -= 1
                if event.key == pygame.K_RETURN:
                    insert_on_board(player_pos, turn)
                    if turn == 1:
                        turn = 2
                    else:
                        turn = 1
    pygame.display.quit()

main()