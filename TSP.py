INF = float ('inf')

distance_matrix = [
#   u   v   w   x   y   z
    [0, 51, 56, 60, 2, 35], # from u
    [51, 0, 78, 13, 51, 68], # from v
    [56, 78, 0, 70, 57, 21], # from w
    [60, 13, 68, 0, 61, 68], # from x
    [2, 51, 57, 61, 0, 36], # from y
    [35, 68, 21, 68, 36, 0]  # from z
]

num_nodes = len(distance_matrix)
nodes = list(range(num_nodes))

# Distance Lookup
def calculate_distance(node1, node2):
    return distance_matrix[node1][node2]

# Calculate total distance of specific route
def total_route_distance(route):
    distance = 0;
    for i in range(len(route) - 1):
        distance += calculate_distance(route[i], route[i+1])
    # add trip back to the start
    distance += calculate_distance(route[-1], route[0])
    return distance

# Nearest neighbor algorithm
def nearest_neighbor(nodes):
    unvisited = list(range(1, len(nodes)))
    route = [0]
    current_node = 0

    while unvisited:
        next_node = min(unvisited, key=lambda node: calculate_distance(current_node, node))
        route.append(next_node)
        unvisited.remove(next_node)
        current_node = next_node

    return route

# 2-Opt logic
def two_opt(route):
    best_route = route
    best_distance = total_route_distance(route)
    improved = True
    iteration = 0

    while improved:
        improved = False
        iteration += 1

        for i in range (1, len(best_route)):
            for j in range(i+1, len(best_route)):
                if j-i == 1: continue

                new_route = best_route[:]
                new_route[i:j]= reversed(best_route[i:j])
                new_distance = total_route_distance(new_route)

                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance
                    improved = True
                    print(f"  -> Iteration {iteration}: Found shorter path! New distance: {best_distance:.2f}")
                    break
            if improved:
                break
    return best_route, best_distance


print("Using explicit distance matrix.\n")

nn_route = nearest_neighbor(nodes)
nn_distance = total_route_distance(nn_route)
print(f"Nearest Neighbor Route: {nn_route} | Distance: {nn_distance}")

opt_route, opt_distance = two_opt(nn_route)
print(f"2-Opt Optimized Route: {opt_route} | Distance: {opt_distance}")
