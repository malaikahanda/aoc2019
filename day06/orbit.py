
class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.children = []

    def count_edges(self):
        c = len(self.children)
        for child in self.children:
            c += child.count_edges()
        return c

    def count_all_edges(self, d=0):
        c = self.count_edges()
        for child in self.children:
            c += child.count_all_edges()
        return c


with open("input.txt") as f:

    orbits = []
    for l in f.readlines():
        l_ = l.strip().split(")")
        orbits.append((l_[0], l_[1]))

    def build_tree(satellite):
        reduced_orbits = [(p, c) for (p, c) in orbits if p == satellite]
        t = TreeNode(satellite)
        for (p, c) in reduced_orbits:
            child = build_tree(c)
            t.children.append(child)
        return t

    tree = build_tree("COM")
    c = tree.count_all_edges()

    print("Count:", c)