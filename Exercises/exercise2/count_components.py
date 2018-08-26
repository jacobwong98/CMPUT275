from graph import Graph
from breadth_first_search import breadth_first_search
# import sys
# import argparse

# parser = argparse.ArgumentParser(
#     description='Text frequency analysis.',
#     formatter_class=argparse.RawTextHelpFormatter
# )
#
# parser.add_argument(
#     "infile",
#     nargs="?",
#     type=argparse.FileType('r'),
#     default=sys.stdin
# )
#
# args = parser.parse_args()


def count_components(g):
    verticesList = g.get_vertices()
    counter = 0

    while len(verticesList) > 0:
        unreachedNodes = verticesList.pop()
        neighbourNodes = breadth_first_search(g, unreachedNodes)
        verticesList -= set(neighbourNodes)
        counter += 1
    return counter


def read_city_graph_undirected(filename):
    with open(filename, 'r') as filename:
        graph = Graph()
        temp = []
        for line in filename:
            temp = line.strip().split(",")
            if temp[0] == 'V':
                graph.add_vertex(temp[1])
            elif temp[0] == 'E':
                graph.add_edge((temp[1], temp[2]))
                graph.add_edge((temp[2], temp[1]))
    return graph


if __name__ == "__main__":
    readGraph = read_city_graph_undirected("edmonton-roads-2.0.1.txt")
    print(count_components(readGraph))
