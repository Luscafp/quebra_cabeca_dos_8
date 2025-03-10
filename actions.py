import pygame
import sys
from utils import draw_grid, draw_text
from config import TILE_SIZE

MOVES = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

def is_valid_move(pos, move):
    """Verifica se o movimento é válido."""
    new_x, new_y = pos[0] + move[0], pos[1] + move[1]
    return 0 <= new_x < 3 and 0 <= new_y < 3

def apply_move(state, pos, move):
    """Aplica um movimento e retorna o novo estado."""
    new_x, new_y = pos[0] + move[0], pos[1] + move[1]
    new_state = [list(row) for row in state]
    new_state[pos[0]][pos[1]], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[pos[0]][pos[1]]
    return tuple(tuple(row) for row in new_state)

def get_manual_state(screen, font):
    """Usuario seleciona o estado inicial"""
    current_state = [[None] * 3 for _ in range(3)]
    remaining_numbers = list(range(9))
    draw_grid(screen, current_state, font)
    draw_text(screen, "Clique para inserir números (0-8)", font, y_offset=-40)

    while remaining_numbers:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row, col = y // TILE_SIZE, x // TILE_SIZE
                if current_state[row][col] is None:
                    number = remaining_numbers.pop(0)
                    current_state[row][col] = number
                    draw_grid(screen, current_state, font)

    return tuple(tuple(row) for row in current_state)
