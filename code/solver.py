from collections import deque

actions = {
    "Kong": [0, 1, 4],
    "Zebra": [0, 1, 2],
    "Ostrich": [1, 2, 3],
    "Snake": [2, 3, 4],
    "Elephant": [0, 3, 4],
}

def solve_to_77777(start:int):
    start -= 11111
    start = [int(d) for d in str(start)]
    goal = [6, 6, 6, 6, 6]

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path  # list of action names in order
        state_tuple = tuple(state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for name, indices in actions.items():
            new_state = state[:]
            for i in indices:
                new_state[i] = (new_state[i] + 1) % 7
            queue.append((new_state, path + [name]))

    return None

l = solve_to_77777(66666)
amount = {}
for s in l:
    if s not in amount:
        amount[s] = 0
    amount[s] += 1
print(amount)