from collections import Counter

import anytree

from helpers import read_raw_entries


def solve_07(entries):
    root = build_tree(entries)
    return root.name


def solve_07b(entries):
    root = build_tree(entries)

    return find_value(root, 0)


def find_value(current_root, last_diff):
    # Check if our children are balanced
    next_node, diff = is_balanced(current_root)

    # If not, we'll be passed back the outlier in the children and the diff it had
    # from it's siblings
    if next_node is not None:
        return find_value(next_node, diff)
    # Otherwise we've found the last part of the chain that is imbalanced,
    # Just need to return the correct weight here
    else:
        return current_root.weight + last_diff


def is_balanced(current_root):
    # Find all the weights of the children
    current_weights = []
    for c in current_root.children:
        current_weights.append(c.total_weight)

    # Collect them into a counter object
    counter = Counter(current_weights)

    # If top and bottom are the same, diff is 0, meaning we're balanced
    diff = counter.most_common()[0][0] - counter.most_common()[-1][0]

    # If we're not balanced, return the outlier node and the diff
    if diff != 0:
        return list(filter(lambda x: x.total_weight == counter.most_common()[-1][0], current_root.children))[0], diff

    # Otherwise return no nodes with diff 0
    return None, 0


def compute_total_weight(node):
    return sum(map(lambda x: x.weight, node.descendants)) + node.weight


def build_tree(entries):
    n = None
    nodes = {}
    for e in entries:
        d = e.replace(',', '').split()

        n = anytree.Node(d[0], None,
                         weight=int(int(str(d[1]).replace('(', '').replace(')', ''))),
                         _children=d[3:])

        nodes[d[0]] = n

    for node in nodes.values():
        for child in node._children:
            nodes[child].parent = node

    for node in nodes.values():
        node.__dict__['total_weight'] = compute_total_weight(node)

    return n.ancestors[0]


if __name__ == '__main__':
    entries = read_raw_entries('input_d7.txt')
    r = solve_07(entries)
    print('part 1, root: {}'.format(r))
    r = solve_07b(entries)
    print('part 2, needed weight: {}'.format(r))
