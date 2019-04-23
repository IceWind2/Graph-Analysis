import xml.etree.ElementTree as ET

person_id = {}
id_person = {}


def person(_local_id):
    global id_person
    return id_person[_local_id]


def local_id(_person):
    global person_id
    return person_id[_person.attrib['id']]


def parse_file(fname, directed=True):
    global person_id, id_person
    x = ET.parse(fname)
    root = x.getroot()[0]

    person_id = {}
    id_person = {}
    cnt = 0
    for p in root[1]:
        person_id[p.attrib['id']] = cnt
        id_person[cnt] = p
        cnt += 1

    mat = []
    for i in range(cnt):
        mat.append([])
    for edge in root[2]:
        mat[person_id[edge.attrib['source']]].append(person_id[edge.attrib['target']])
        if not directed:
            mat[person_id[edge.attrib['target']]].append(person_id[edge.attrib['source']])

    return mat, id_person
