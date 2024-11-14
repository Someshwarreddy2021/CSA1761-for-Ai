def is_safe(node, color, assignment, constraints):
    for neighbor in constraints[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, nodes, colors, constraints):
    if len(assignment) == len(nodes):
        return assignment

    unassigned_nodes = [node for node in nodes if node not in assignment]
    node = unassigned_nodes[0]

    for color in colors:
        if is_safe(node, color, assignment, constraints):
            assignment[node] = color
            result = backtrack(assignment, nodes, colors, constraints)
            if result:
                return result
            del assignment[node]
    return None

def map_coloring(nodes, colors, constraints):
    return backtrack({}, nodes, colors, constraints)

nodes = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
colors = ['Red', 'Green', 'Blue']
constraints = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

solution = map_coloring(nodes, colors, constraints)

if solution:
    print("Coloring solution found:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution found")
