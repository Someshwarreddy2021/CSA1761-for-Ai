from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_capacity):
    queue = deque([(0, 0, [])])  # (jug1, jug2, steps)
    visited = set((0, 0))

    while queue:
        jug1, jug2, steps = queue.popleft()

        if jug1 == target_capacity or jug2 == target_capacity:
            return steps + [(jug1, jug2)]

        # Fill jug1
        if jug1 < jug1_capacity:
            new_state = (jug1_capacity, jug2, steps + [(jug1_capacity, jug2)])
            if (jug1_capacity, jug2) not in visited:
                queue.append(new_state)
                visited.add((jug1_capacity, jug2))

        # Fill jug2
        if jug2 < jug2_capacity:
            new_state = (jug1, jug2_capacity, steps + [(jug1, jug2_capacity)])
            if (jug1, jug2_capacity) not in visited:
                queue.append(new_state)
                visited.add((jug1, jug2_capacity))

        # Empty jug1
        if jug1 > 0:
            new_state = (0, jug2, steps + [(0, jug2)])
            if (0, jug2) not in visited:
                queue.append(new_state)
                visited.add((0, jug2))

        # Empty jug2
        if jug2 > 0:
            new_state = (jug1, 0, steps + [(jug1, 0)])
            if (jug1, 0) not in visited:
                queue.append(new_state)
                visited.add((jug1, 0))

        # Pour jug1 to jug2
        pour_amount = min(jug1, jug2_capacity - jug2)
        new_jug1 = jug1 - pour_amount
        new_jug2 = jug2 + pour_amount
        new_state = (new_jug1, new_jug2, steps + [(new_jug1, new_jug2)])
        if (new_jug1, new_jug2) not in visited:
            queue.append(new_state)
            visited.add((new_jug1, new_jug2))

        # Pour jug2 to jug1
        pour_amount = min(jug2, jug1_capacity - jug1)
        new_jug1 = jug1 + pour_amount
        new_jug2 = jug2 - pour_amount
        new_state = (new_jug1, new_jug2, steps + [(new_jug1, new_jug2)])
        if (new_jug1, new_jug2) not in visited:
            queue.append(new_state)
            visited.add((new_jug1, new_jug2))

    return None

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target_capacity = 2

solution = water_jug_problem(jug1_capacity, jug2_capacity, target_capacity)

if solution:
    print("Solution:")
    for i, (jug1, jug2) in enumerate(solution):
        print(f"Step {i+1}: Jug1 = {jug1}, Jug2 = {jug2}")
else:
    print("No solution found.")
