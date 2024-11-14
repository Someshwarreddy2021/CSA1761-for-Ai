from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if (self.missionaries < self.cannibals and self.missionaries > 0) or (self.missionaries > self.cannibals and self.missionaries < 3):
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def get_successors(self):
        successors = []
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            if self.boat == 1:
                new_state = State(self.missionaries - m, self.cannibals - c, 0, self)
            else:
                new_state = State(self.missionaries + m, self.cannibals + c, 1, self)
            if new_state.is_valid():
                successors.append(new_state)
        return successors

def bfs():
    initial_state = State(3, 3, 1)
    if initial_state.is_goal():
        return initial_state
    frontier = deque([initial_state])
    explored = set()
    while frontier:
        state = frontier.popleft()
        explored.add((state.missionaries, state.cannibals, state.boat))
        for successor in state.get_successors():
            if (successor.missionaries, successor.cannibals, successor.boat) not in explored:
                if successor.is_goal():
                    return successor
                frontier.append(successor)
    return None

def print_solution(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    for s in reversed(path):
        print(f"Missionaries: {s.missionaries}, Cannibals: {s.cannibals}, Boat: {s.boat}")

solution = bfs()
if solution:
    print_solution(solution)
else:
    print("No solution found")
