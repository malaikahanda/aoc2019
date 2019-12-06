
class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.children = []

    def count_edges(self):
        c = len(self.children)
        for child in self.children:
            c += child.count_edges()
        return c

    def dist_to(self, val):
        if self.val == val:
            return 0
        for child in self.children:
            if child.contains(val):
                return 1 + child.dist_to(val)

    def contains(self, val):
        if self.val == val:
            return True
        for child in self.children:
            if child.contains(val):
                return True
        return False



with open("input.txt") as f:

    orbits = []
    for l in f.readlines():
        l_ = l.strip().split(")")
        orbits.append((l_[0], l_[1]))

    START = [(p, c) for (p, c) in orbits if c == "YOU"][0][0]
    END = [(p, c) for (p, c) in orbits if c == "SAN"][0][0]

    def build_tree(satellite):
        reduced_orbits = [(p, c) for (p, c) in orbits if p == satellite]
        t = TreeNode(satellite)
        for (p, c) in reduced_orbits:
            child = build_tree(c)
            t.children.append(child)
        return t

    tree = build_tree("COM")

    best_size = [10000000000000000000000000000000]
    best_tree = [None]
    def find_sub_tree(t):
        if t.contains(START) and t.contains(END):
            size = t.count_edges()
            if size < best_size[0]:
                best_size[0] = size
                best_tree[0] = t
        for c in t.children:
            find_sub_tree(c)
        return
    
    find_sub_tree(tree)

    best_tree = best_tree.pop()
    print(best_tree.dist_to(START) + best_tree.dist_to(END))