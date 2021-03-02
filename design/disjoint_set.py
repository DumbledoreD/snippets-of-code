import collections


class DisjointSet:
    def __init__(self):
        # Parent node has value None
        self.child_to_parent = collections.defaultdict(lambda: None)

    def find(self, val):
        parent = self.child_to_parent[val]

        # val is the parent
        if parent is None:
            return val

        true_parent = self.find(parent)
        # Collapsing find
        self.child_to_parent[val] = true_parent

        return true_parent

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        self.child_to_parent[y] = x_parent
