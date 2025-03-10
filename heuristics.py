def heuristic(state, goal_state):
    """Heurística de Manhattan para o quebra-cabeça dos 8."""
    total_distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_pos = [(x, y) for x, row in enumerate(goal_state) for y, val in enumerate(row) if val == value][0]
                total_distance += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return total_distance