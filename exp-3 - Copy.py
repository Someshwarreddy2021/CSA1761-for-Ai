# Set the capacities of Jug 1, Jug 2, and the target amount
jug1 = 4
jug2 = 3
target = 2

# We will use a list to keep track of visited states to avoid repeating them
visited_states = []

# This function checks if we have reached the target amount in either jug
def is_target_reached(x, y):
    return x == target or y == target

# This function finds a solution using a step-by-step approach
def solve_water_jug():
    # Start with both jugs empty
    queue = [(0, 0)]  # Queue of states (water in jug1, water in jug2)

    # Keep exploring until the queue is empty
    while queue:
        # Get the current state of the jugs
        x, y = queue.pop(0)

        # If this state has already been visited, skip it
        if (x, y) in visited_states:
            continue

        # Mark this state as visited
        visited_states.append((x, y))
        print(f"Checking state: Jug1 = {x}, Jug2 = {y}")

        # Check if we have reached the target
        if is_target_reached(x, y):
            print(f"Target of {target} liters reached!")
            return

        # Possible moves to create new states
        possible_moves = [
            (jug1, y),          # Fill Jug 1
            (x, jug2),          # Fill Jug 2
            (0, y),             # Empty Jug 1
            (x, 0),             # Empty Jug 2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour Jug 1 into Jug 2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour Jug 2 into Jug 1
        ]

        # Add each possible move to the queue
        for move in possible_moves:
            if move not in visited_states:
                queue.append(move)

    print("Target cannot be reached with given jug sizes.")

# Run the solution
solve_water_jug()
