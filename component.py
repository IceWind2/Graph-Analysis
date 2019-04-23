components = []
marked = []


def dfs(v, mat, color):
    global marked, components
    marked[v] = True
    components[v] = color
    for e in mat[v]:
        if not marked[e]:
            dfs(e, mat, color)
    return


def component(matrix):
    global marked, components
    cnt = len(matrix)
    marked = [False] * cnt
    components = [0] * cnt
    color = 0
    for i in range(cnt):
        if not marked[i]:
            dfs(i, matrix, color)
            color += 1

    comp_count = {}
    for q in components:
        if q in comp_count:
            comp_count[q] += 1
        else:
            comp_count[q] = 1

    max_count = comp_count[0]
    max_comp = 0
    for i, c in comp_count.items():
        if max_count < c:
            max_count = c
            max_comp = i

    return components, comp_count, max_comp
