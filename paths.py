class Graph_Description:

    def __init__(self):
        self.radius = None
        self.diameter = None
        self.central_vertices = []
        self.periferal_vertices = []
        self.mean_path_length = None

    def show(self):
        print("min dist ", self.radius, ': ', self.central_vertices)
        print("max dist ", self.diameter, ': ', self.periferal_vertices)
        print("mean dist ", self.mean_path_length)


class queue:
    _q = None

    def __init__(self):
        self._q = []

    def push(self, x):
        self._q.append(x)

    def pop(self):
        if len(self._q) == 0:
            return
        self._q.remove(self._q[0])

    def top(self):
        if len(self._q) == 0:
            return None
        return self._q[0]

    def __len__(self):
        return len(self._q)

    def items(self):
        return [*self._q]


def mean(list):
    return sum(list) / len(list)


def calculate_paths(matrix):
    q = queue()
    N = len(matrix)
    vert_dist = []

    for i in range(N):
        marked = [False] * N
        marked[i] = True
        q.push(i)
        dist = -1

        while q.top() is not None:
            dist += 1
            q2 = queue()
            while q.top() is not None:
                tmp = q.top()
                marked[tmp] = True
                for j in range(len(matrix[tmp])):
                    if not marked[matrix[tmp][j]]:
                        q2.push(matrix[tmp][j])
                        marked[matrix[tmp][j]] = True
                q.pop()

            for el in q2.items():
                q.push(el)

        vert_dist.append(dist)

    result = Graph_Description()
    result.radius = min(vert_dist)
    result.diameter = max(vert_dist)
    result.central_vertices = [i for i in range(N) if vert_dist[i] == result.radius]
    result.periferal_vertices = [i for i in range(N) if vert_dist[i] == result.diameter]
    result.mean_path_length = mean(vert_dist)

    return result
