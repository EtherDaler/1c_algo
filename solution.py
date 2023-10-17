from collections import defaultdict

visited = set()
infected = set()
min_infected = set()

# функция для создания графа
def create_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def dfs(graph, v):
    global visited
    if v not in visited:
        visited.add(v)
        for neighbour in graph[v]:
            dfs(graph, neighbour)

# функция для проверки условий заражения
def is_infected(graph, node):
    global infected
    if node in infected:
        return True
    cnt = 0
    for neighbor in graph[node]:
        if neighbor in infected:
            cnt += 1
        if cnt == 2:
            return True
    return False

# функция для поиска минимального количества городов, которые нужно заразить
def find_min_infected(graph):
    global infected, min_infected
    nodes = set(graph.keys())
    d = {
        i: len(graph[i])
        for i in min_infected
    }
    s_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
    cur_min = [el[0] for el in s_d]
    for ill in cur_min:
        m = 0
        el = None
        for neighbour in graph[ill]:
            if neighbour in infected:
                continue
            if len(graph[neighbour]) > m:
                m = len(graph[neighbour])
                el = neighbour
        if el != None:
            infected.add(el)
            min_infected.add(el)

        for node in nodes:
            if is_infected(graph, node):
                infected.add(node)

# пример использования
n = int(input())
edges = list()

# Ввод и создание графа
for i in range(n):
    edge = tuple([int(x) for x in input().split()])
    edges.append(edge)
graph = create_graph(edges)

# Запускаем DFS и помечаем заражаем первые вершины в каждой компоненте связности
for i in graph.keys():
    if i not in visited:
        infected.add(i)
        min_infected.add(i)
        dfs(graph, i)

while(len(infected) < len(graph.keys())):
    find_min_infected(graph)
print(len(min_infected))

print(', '.join([str(el) for el in min_infected]))