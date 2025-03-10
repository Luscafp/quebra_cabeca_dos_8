import heapq
from state import find_zero
from actions import is_valid_move, apply_move, MOVES
from heuristics import heuristic

def a_star(initial_state, goal_state):
    """Resolve o quebra-cabeça dos 8 usando o algoritmo A*."""
    priority_queue = []
    heapq.heappush(priority_queue, (0, initial_state, 0, None))
    visited = set()
    came_from = {}

    while priority_queue:
        _, current_state, cost, prev_state = heapq.heappop(priority_queue)

        if current_state in visited:
            continue

        visited.add(current_state)
        came_from[current_state] = prev_state

        if current_state == goal_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = came_from[current_state]
            return path[::-1]

        zero_pos = find_zero(current_state)

        for move_name, move_delta in MOVES.items():
            if is_valid_move(zero_pos, move_delta):
                new_state = apply_move(current_state, zero_pos, move_delta)
                if new_state not in visited:
                    new_cost = cost + 1
                    priority = new_cost + heuristic(new_state, goal_state)
                    heapq.heappush(priority_queue, (priority, new_state, new_cost, current_state))

    return None