import pygame
import sys
from puzzle_solver import a_star
from state import GOAL_STATE, is_solvable, generate_random_state
from utils import draw_grid, draw_buttons
from actions import get_manual_state
from config import WINDOW_SIZE, FONT_SIZE, FPS

def main():
    """Função principal da interface gráfica."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Quebra-Cabeça dos 8")
    font = pygame.font.Font(None, FONT_SIZE)
    clock = pygame.time.Clock()

    while True:
        button_areas = draw_buttons(screen, ["Criar Estado", "Gerar Estado"], font, y_offset=-40)

        choice = None
        while choice is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for text, rect in button_areas:
                        if rect.collidepoint(mouse_pos):
                            if text == "Criar Estado":
                                choice = 1
                            elif text == "Gerar Estado":
                                choice = 2

            button_areas = draw_buttons(screen, ["Criar Estado", "Gerar Estado"], font, y_offset=-40)

        if choice == 1:
            initial_state = get_manual_state(screen, font)
            if not is_solvable(initial_state):
                draw_buttons(screen, ["Estado não solúvel!", "Tente novamente."], font, y_offset=-40)
                pygame.time.wait(2000)
                continue
        else:
            initial_state = generate_random_state()

        solution_path = a_star(initial_state, GOAL_STATE)

        if not solution_path:
            draw_buttons(screen, ["Nenhuma solução encontrada!"], font, y_offset=-40)
            pygame.time.wait(2000)
            continue

        total_steps = len(solution_path) - 1

        for step_index, state in enumerate(solution_path):
            draw_grid(screen, state, font, step_index=step_index, total_steps=total_steps)
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        button_areas = draw_buttons(screen, [f"Solução em {len(solution_path) - 1} passos.", "Tentar novamente?"], font, y_offset=-40)

        retry = None
        while retry is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for text, rect in button_areas:
                        if rect.collidepoint(mouse_pos):
                            if "Tentar novamente" in text:
                                retry = True

            button_areas = draw_buttons(screen, [f"Solução em {len(solution_path) - 1} passos.", "Tentar novamente?"], font, y_offset=-40)

        if not retry:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
