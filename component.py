components = []
marked = []
vert_time = []
deleted = []
time = 0


def dfs(v, mat, color):
    global marked, components, deleted
    marked[v] = True
    if color != -1:
        components[v] = color
    for e in mat[v]:
        if not marked[e]:
            if len(deleted) > 0 and deleted[e]:
                continue
            dfs(e, mat, color)

    return


def inverted_dfs(v, mat):
    global marked, deleted, time
    marked[v] = True
    for i in range(len(mat)):
        if not deleted[i] and v in mat[i] and not marked[i]:
            inverted_dfs(i, mat)
    vert_time[v] = time
    time += 1


def get_components(matrix):
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


def get_strong_components(matrix):
    global marked, vert_time, deleted, time
    cnt = len(matrix)
    deleted = [False] * cnt
    colors = [-1] * cnt
    color = 0
    while False in deleted:
        marked = [False] * cnt
        vert_time = [0] * cnt
        time = 1
        for i in range(cnt):
            if not deleted[i] and not marked[i]:
                inverted_dfs(i, matrix)

        marked = [False] * cnt
        dfs(vert_time.index(max(vert_time)), matrix, -1)
        for i in range(cnt):
            if marked[i]:
                deleted[i] = True
                colors[i] = color
        color += 1

    color_count = {}
    for q in colors:
        if q in color_count:
            color_count[q] += 1
        else:
            color_count[q] = 1

    return colors, color_count
