from collections import deque

# Define the target goal state of the puzzle
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the blank space

# Define the possible moves for the blank tile
moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Function to find the position of the blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to check if the puzzle state matches the goal state
def is_goal(state):
    return state == goal_state

# Function to generate the new state after moving the blank tile
def move_blank(state, direction):
    i, j = find_blank(state)
    new_state = [row[:] for row in state]
    di, dj = moves[direction]
    new_i, new_j = i + di, j + dj

    # Check if the new position is within the grid bounds
    if 0 <= new_i < 3 and 0 <= new_j < 3:
        # Swap the blank tile with the target tile
        new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
        return new_state
    return None  # Invalid move

# BFS function to solve the puzzle
def bfs(start_state):
    queue = deque([(start_state, [])])  # Queue stores (current_state, path_to_current_state)
    visited = set()
    visited.add(tuple(tuple(row) for row in start_state))  # Use tuples for hashing

    while queue:
        current_state, path = queue.popleft()

        if is_goal(current_state):
            return path  # Return the sequence of moves to reach the goal

        # Try all possible moves
        for direction in moves:
            new_state = move_blank(current_state, direction)
            if new_state and tuple(tuple(row) for row in new_state) not in visited:
                visited.add(tuple(tuple(row) for row in new_state))
                queue.append((new_state, path + [direction]))

    return None  # No solution found

# Sample initial state
start_state = [[1, 2, 3],
               [4, 0, 5],
               [7, 8, 6]]

# Solve the puzzle
solution = bfs(start_state)
if solution:
    print("Solution found:")
    print(" -> ".join(solution))
else:
    print("No solution exists.")
