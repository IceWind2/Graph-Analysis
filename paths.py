class GraphDescription:
    def __init__(self):
        self.radius = None
        self.diameter = None
        self.central_vertices = []
        self.peripheral_vertices = []
        self.mean_path_length = None
        self.distances = []

    def __calculate_distances(self, matrix):
        # TODO: replace custom queue with built in
        q = queue()
        n = len(matrix)
        vert_dist = []

        for i in range(n):
            marked = [False] * n
            marked[i] = True
            q.push(i)
            dist = -1
            cur_dist = [0] * n

            while q.top() is not None:
                dist += 1
                q2 = queue()
                while q.top() is not None:
                    cur_vert = q.top()
                    cur_dist[cur_vert] = dist
                    marked[cur_vert] = True

                    for j in range(len(matrix[cur_vert])):
                        if not marked[matrix[cur_vert][j]]:
                            q2.push(matrix[cur_vert][j])
                            marked[matrix[cur_vert][j]] = True
                    q.pop()

                for el in q2.items():
                    q.push(el)

            vert_dist.append(cur_dist)

        self.distances = vert_dist

    def show(self):
        print("min dist ", self.radius, ': ', self.central_vertices)
        print("max dist ", self.diameter, ': ', self.peripheral_vertices)
        print("mean dist ", self.mean_path_length)

    def create_description(self, matrix):
        self.__calculate_distances(matrix)
        self.radius = min([max(person) for person in self.distances])
        self.diameter = max([max(person) for person in self.distances])
        self.central_vertices = [i for i in range(len(self.distances)) if max(self.distances[i]) == self.radius]
        self.peripheral_vertices = [i for i in range(len(self.distances)) if max(self.distances[i]) == self.diameter]
        self.mean_path_length = mean([mean(person) for person in self.distances])


def get_description(matrix):
        result = GraphDescription()
        result.create_description(matrix)
        return result


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


def mean(l):
    return sum(l) / len(l)
