# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# https://www.techiedelight.com/breadth-first-search/
from collections import deque

example_graph = {
    "A": set(["B", "C"]),
    "B": set(["A", "D", "E"]),
    "C": set(["A", "F"]),
    "D": set(["B"]),
    "E": set(["B", "F"]),
    "F": set(["C", "E"]),
}


# Depth-First Search


def dfs_stack(graph, start):
    visited, stack = set(), [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


print(dfs_stack(example_graph, "A"))


def dfs_rec(graph, vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(vertex)

    for next_vertex in graph[vertex] - visited:
        dfs_rec(graph, next_vertex, visited)

    return visited


print(dfs_rec(example_graph, "A"))


def dfs_stack_path(graph, start, goal):
    stack = [(start, [start])]

    while stack:
        vertex, path = stack.pop()
        for next_vertex in graph[vertex] - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            else:
                stack.append((next_vertex, path + [next_vertex]))


print(list(dfs_stack_path(example_graph, "A", "F")))


def dfs_rec_path(graph, vertex, goal, path=None):
    if path is None:
        path = [vertex]

    if vertex == goal:
        yield path

    for next_vertex in graph[vertex] - set(path):
        yield from dfs_rec_path(graph, next_vertex, goal, path + [next_vertex])


print(list(dfs_rec_path(example_graph, "A", "F")))


# Breath-First Search


def bfs_queue(graph, start):
    visited, queue = set(), deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


print(bfs_queue(example_graph, "A"))


def bfs_rec(graph, queue, visited=None):
    if visited is None:
        visited = set()

    if not queue:
        return visited

    vertex = queue.popleft()
    visited.add(vertex)
    queue.extend(graph[vertex] - visited)
    return bfs_rec(graph, queue, visited)


print(bfs_rec(example_graph, deque(["A"])))


def bfs_queue_path(graph, start, goal):
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()
        for next_vertex in graph[vertex] - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            else:
                queue.append((next_vertex, path + [next_vertex]))


print(list(bfs_queue_path(example_graph, "A", "F")))


def bfs_rec_path(graph, queue, goal):
    if queue:
        vertex, path = queue.popleft()

        if vertex == goal:
            yield path

        for next_vertex in graph[vertex] - set(path):
            queue.append((next_vertex, path + [next_vertex]))

        yield from bfs_rec_path(graph, queue, goal)


print(list(bfs_rec_path(example_graph, deque([("A", ["A"])]), "F")))
