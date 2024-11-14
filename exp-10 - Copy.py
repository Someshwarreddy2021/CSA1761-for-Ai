from queue import PriorityQueue

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic from this node to the goal
        self.f = 0  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

def a_star(graph, start, goal):
    open_list = PriorityQueue()
    open_list.put(Node(start))
    closed_list = set()
    start_node = Node(start)
    goal_node = Node(goal)
    
    while not open_list.empty():
        current_node = open_list.get()
        closed_list.add(current_node.position)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor_pos = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])
            if neighbor_pos in closed_list or neighbor_pos not in graph:
                continue
            
            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.g = current_node.g + graph[neighbor_pos]
            neighbor_node.h = abs(neighbor_pos[0] - goal_node.position[0]) + abs(neighbor_pos[1] - goal_node.position[1])
            neighbor_node.f = neighbor_node.g + neighbor_node.h
            
            if any(open_node.position == neighbor_node.position and open_node.f <= neighbor_node.f for open_node in open_list.queue):
                continue
            
            open_list.put(neighbor_node)
    
    return None

graph = {
    (0, 0): 1, (0, 1): 1, (0, 2): 1, (0, 3): 1,
    (1, 0): 1, (1, 1): 1, (1, 2): 1, (1, 3): 1,
    (2, 0): 1, (2, 1): 1, (2, 2): 1, (2, 3): 1,
    (3, 0): 1, (3, 1): 1, (3, 2): 1, (3, 3): 1
}

start = (0, 0)
goal = (3, 3)
path = a_star(graph, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found")
