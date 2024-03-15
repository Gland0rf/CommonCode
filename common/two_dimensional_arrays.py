import heapq

def heuristic(node, goal):
    return ((node[0] - goal[0])**2 + (node[1] - goal[1])**2)**0.5

def get_neighbors(node, grid):
    possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbors = []
    for move in possible_moves:
        new_node = (node[0] + move[0], node[1] + move[1])
        if 0 <= new_node[0] < len(grid) and 0 <= new_node[1] < len(grid[0]) and grid[new_node[0]][new_node[1]] != 1:
            neighbors.append(new_node)
    return neighbors

def astar(start, goal, grid, onlyCheckIfPathFound, containsFirstValue):
    open_set = [(0, start)]
    closed_set = set()
    g_values = {start: 0}
    parents = {}

    if grid[start[0]][start[1]] == 1: 
        if onlyCheckIfPathFound: return False
        return None

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in parents:
                path.insert(0, current)
                current = parents[current]
            if containsFirstValue: path.insert(0, start)

            if onlyCheckIfPathFound: return True
            return path

        closed_set.add(current)

        for neighbor in get_neighbors(current, grid):
            if neighbor in closed_set:
                continue

            tentative_g = g_values[current] + 1  # Assuming a cost of 1 for each movement
            if neighbor not in [item[1] for item in open_set] or tentative_g < g_values[neighbor]:
                g_values[neighbor] = tentative_g
                f_value = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_value, neighbor))
                parents[neighbor] = current

    if(onlyCheckIfPathFound): return False
    else: return None

class pathfinding:
    def getSteps(grid, start, goal, containsFirstValue):
        '''
        Prints all the steps needed to get from one pos to another\n
        Grid - The Grid in the form of a 2d array\n
        Start - A Tuple with a Y and X Coordinate (FIRST y THEN x)\n
        Goal - The goal position; Input like Start\n
        ContainsFirstValue - True or False wheter the first value should be in the output. Return a boolean
        '''
        path = astar(start, goal, grid, False, containsFirstValue)
        return path
    def checkForPath(grid, start, goal):
        '''
        Just tells you if there is a possible path\n
        Grid - The Grid in the form of a 2d array\n
        Start - A Tuple with a Y and X Coordinate (FIRST y THEN x)\n
        Goal - The goal position; Input like Start
        '''
        path = astar(start, goal, grid, True, False)
        return path