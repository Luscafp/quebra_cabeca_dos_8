import random

GOAL_STATE = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))

def find_zero(state):
    for i, row in enumerate(state):
        for j, value in enumerate(row):
            if value == 0:
                return i, j

def is_solvable(state):
    """Verifica se um estado é solucionável."""
    flat_state = [num for row in state for num in row if num != 0]
    inversions = sum(1 for i in range(len(flat_state)) for j in range(i + 1, len(flat_state)) if flat_state[i] > flat_state[j])
    return inversions % 2 == 0

def generate_random_state():
    """Gera um estado inicial aleatório que seja solucionável."""
    while True:
        numbers = list(range(9))
        random.shuffle(numbers)
        state = tuple(tuple(numbers[i:i + 3]) for i in range(0, 9, 3))
        if is_solvable(state): 
            return state