from itertools import permutations

def calculate_route_cost(graph, route):
    cost = 0
    for i in range(len(route) - 1):
        cost += graph[route[i]][route[i + 1]]
    cost += graph[route[-1]][route[0]]  # Return to starting city
    return cost

def tsp(graph, start=0):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_cost = float('inf')
    best_route = None
    
    for perm in permutations(nodes):
        route = [start] + list(perm)
        current_cost = calculate_route_cost(graph, route)
        if current_cost < min_cost:
            min_cost = current_cost
            best_route = route
            
    return best_route, min_cost

graph = {
    0: {1: 10, 2: 15, 3: 20},
    1: {0: 10, 2: 35, 3: 25},
    2: {0: 15, 1: 35, 3: 30},
    3: {0: 20, 1: 25, 2: 30}
}

start_city = 0
best_route, min_cost = tsp(graph, start_city)

print("Best Route:", best_route)
print("Minimum Cost:", min_cost)
