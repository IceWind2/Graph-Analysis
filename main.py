from component import *
from input import *
from paths import *
from similarity import *
import matplotlib.pyplot as plt


def get_degrees(matrix):
    deg = {}
    for person in matrix:
        if len(person) not in deg:
            deg[len(person)] = 1
        else:
            deg[len(person)] += 1

    return deg


if __name__ == "__main__":
    # Load graph data into adjacency matrix
    mat, id_person = parse_file('qq.gexf')
    cnt = len(mat)

    # -------------------------------------TASK 1-------------------------------------
    print('TASK 1')

    # Calculate components
    vert_comp, comp_count, main_comp = get_components(mat)
    print(vert_comp)
    print(comp_count)
    print(comp_count[main_comp] / cnt * 100, '%')
    strong_comp, strong_count = get_strong_components(mat)
    print(strong_comp)
    print(strong_count, '\n')

    # Exclude everything but main component
    new_idx = {}
    old_idx = {}
    diff = 0
    for i in range(cnt):
        if vert_comp[i] == main_comp:
            new_idx[i] = i - diff
            old_idx[i - diff] = i
        else:
            diff += 1

    new_mat = []
    for i in range(cnt):
        if vert_comp[i] == main_comp:
            new_mat.append([])
            for q in range(len(mat[i])):
                if new_idx[mat[i][q]] is not None:
                    new_mat[-1].append(new_idx[mat[i][q]])
    mat = new_mat
    cnt = len(mat)

    for i in range(cnt):
        for p in mat[i]:
            if i not in mat[p]:
                mat[p].append(i)

    # -------------------------------------TASK 2-------------------------------------
    print('TASK 2')

    # Calculate vertex degree distribution
    degree_count = get_degrees(mat)
    plt.hist(list(degree_count.keys()), weights=[i / cnt for i in degree_count.values()], bins=max(list(degree_count)), rwidth=0.65, align='left')
    plt.xlabel('degree')
    plt.ylabel('probability')
    plt.savefig('degree distribution.png')

    # Calculate distance parameters
    vert_dist = get_description(mat)
    vert_dist.show()
    print([id_person[idx].attrib['label'] for idx in [old_idx[el] for el in vert_dist.central_vertices]])

    # -------------------------------------TASK 3-------------------------------------
    print('TASK 3')

    sim = similarity_measures(mat)
    print(*sim.neighbors, sep='\n')
    print(id_person[old_idx[13]].attrib['label'])