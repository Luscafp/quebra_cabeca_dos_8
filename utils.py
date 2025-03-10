import pygame
import matplotlib.pyplot as plt
from config import (
    WINDOW_SIZE,
    TILE_SIZE,
    BG_GRADIENT_TOP,
    BG_GRADIENT_BOTTOM,
    TILE_COLOR,
    TILE_HIGHLIGHT,
    FONT_COLOR,
    EMPTY_TILE_COLOR,
    BG_COLOR,
    BUTTON_COLOR,
    HOVER_BUTTON_COLOR,
)

def draw_gradient(screen):
    for y in range(WINDOW_SIZE):
        color = [
            BG_GRADIENT_TOP[i] + (BG_GRADIENT_BOTTOM[i] - BG_GRADIENT_TOP[i]) * y // WINDOW_SIZE
            for i in range(3)
        ]
        pygame.draw.line(screen, color, (0, y), (WINDOW_SIZE, y))

def calculate_tile_color(step_index, total_steps, base_color):
    """
    Calcula a cor de um bloco com base no índice do passo atual.
    Retorna um gradiente entre a cor base e uma cor mais clara.
    """
    factor = step_index / total_steps if total_steps > 0 else 0
    return tuple(int(c * (1 - factor) + 100 * factor) for c in base_color)

def draw_grid(screen, state, font, step_index=0, total_steps=1):
    """Desenha o tabuleiro com estilo de blocos 3D e cores dinâmicas."""
    draw_gradient(screen)
    for i, row in enumerate(state):
        for j, value in enumerate(row):
            tile_color = TILE_COLOR if value != 0 else EMPTY_TILE_COLOR
            if value != 0:
                tile_color = calculate_tile_color(step_index, total_steps, TILE_COLOR)

            rect = pygame.Rect(j * TILE_SIZE + 10, i * TILE_SIZE + 10, TILE_SIZE - 20, TILE_SIZE - 20)

            if value != 0:
                shadow_rect = rect.move(5, 5)
                pygame.draw.rect(screen, (30, 30, 50), shadow_rect, border_radius=12)
                pygame.draw.rect(screen, tile_color, rect, border_radius=12)

                highlight_rect = rect.inflate(-5, -5)
                pygame.draw.rect(screen, TILE_HIGHLIGHT, highlight_rect, border_radius=12)

                text_surface = font.render(str(value), True, FONT_COLOR)
                text_rect = text_surface.get_rect(center=rect.center)
                screen.blit(text_surface, text_rect)
            else:
                pygame.draw.rect(screen, tile_color, rect, border_radius=12)

    pygame.display.flip()

def draw_text(screen, texts, font, y_offset=0):
    """Desenha um ou mais textos centralizados na tela."""
    screen.fill(BG_COLOR)
    if isinstance(texts, str):
        texts = [texts]

    for i, text in enumerate(texts):
        text_surface = font.render(text, True, FONT_COLOR)
        text_rect = text_surface.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2 + y_offset + i * 40))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

def draw_buttons(screen, texts, font, y_offset=0):
    """Desenha botões estilizados com animação."""
    button_areas = []
    draw_gradient(screen)

    for i, text in enumerate(texts):
        text_surface = font.render(text, True, FONT_COLOR)
        text_rect = text_surface.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2 + y_offset + i * 80))
        button_rect = text_rect.inflate(30, 20)

        mouse_pos = pygame.mouse.get_pos()
        color = HOVER_BUTTON_COLOR if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR

        pygame.draw.rect(screen, color, button_rect, border_radius=15)
        pygame.draw.rect(screen, FONT_COLOR, button_rect, width=2, border_radius=15)
        screen.blit(text_surface, text_rect)

        button_areas.append((text, button_rect))

    pygame.display.flip()
    return button_areas