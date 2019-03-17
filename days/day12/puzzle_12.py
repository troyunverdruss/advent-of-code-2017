import networkx as nx

from helpers import read_raw_entries


class Node:
    def __init__(self, id):
        self.id = id


def solve_12(entries):
    graph, nodes = build_graph(entries)
    return 1 + len(nx.descendants(graph, nodes[0]))


def solve_12b(entries):
    graph, nodes = build_graph(entries)
    groups = 0
    all_programs = nodes.keys()

    while len(all_programs) > 0:
        groups += 1

        node_id = min(all_programs)
        all_programs -= {node_id}

        # Nodes that only connected to themselves were omitted from the graph
        if nodes[node_id] in graph:
            reachable = nx.descendants(graph, nodes[node_id])
            all_programs -= set(map(lambda x: x.id, reachable))

    return groups


def build_graph(entries):
    nodes = {}
    graph = nx.Graph()
    for entry in entries:
        vals = list(map(lambda x: x.replace(',', ''), entry.split()))
        parent = int(vals[0])
        children = map(int, vals[2:])

        # Not adding nodes that only reach themselves
        if parent not in nodes:
            nodes[parent] = Node(parent)

        for c in children:
            if c not in nodes:
                nodes[c] = Node(c)

            if parent == c:
                continue

            if parent < c:
                graph.add_edge(nodes[parent], nodes[c])
            else:
                graph.add_edge(nodes[c], nodes[parent])
    return graph, nodes


if __name__ == '__main__':
    entries = read_raw_entries('input_12.txt')
    r = solve_12(entries)
    print('part 1, all relations to 0: {}'.format(r))
    r = solve_12b(entries)
    print('part 2, total groups: {}'.format(r))
