class Similarity:
    def __init__(self):
        self.__graph = []
        self.neighbors = None
        self.jaccard = None
        self.adamic = None
        self.preferential = None

    def __common_neighbors(self):
        result = []
        for neighbors_x in self.__graph:
            tmp = []
            for neighbors_y in self.__graph:
                tmp.append(len(set(neighbors_x) & set(neighbors_y)))
            result.append(tmp)
        self.neighbors = result

    def __jaccards_coefficient(self):
        if self.neighbors is None:
            self.common_neighbors()

        result = []
        for i, neighbors_x in enumerate(self.__graph):
            tmp = []
            for j, neighbors_y in enumerate(self.__graph):
                union_cnt = len(set(neighbors_x) | set(neighbors_y))
                tmp.append(self.neighbors[i][j]/union_cnt)
            result.append(tmp)
        self.jaccard = result

    def __frequency_weighted(self):
        result = []
        for neighbors_x in self.__graph:
            tmp = []
            for neighbors_y in self.__graph:
                summ = 0
                for person in set(neighbors_x) & set(neighbors_y):
                    summ += len(self.__graph[person])
                tmp.append(summ)
            result.append(tmp)
        self.adamic = result

    def __preferential_attachment(self):
        result = []
        for neighbors_x in self.__graph:
            tmp = []
            for neighbors_y in self.__graph:
                tmp.append(len(neighbors_x) * len(neighbors_y))
            result.append(tmp)
        self.preferential = result

    def calculate_similarities(self, matrix):
        self.__graph = matrix
        self.__common_neighbors()
        self.__jaccards_coefficient()
        self.__frequency_weighted()
        self.__preferential_attachment()


def similarity_measures(matrix):
    sim = Similarity()
    sim.calculate_similarities(matrix)
    return sim
