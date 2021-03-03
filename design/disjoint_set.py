import collections


class DisjointSet:
    def __init__(self):
        # Parent node has value None
        self.child_to_parent = collections.defaultdict(lambda: None)

    def __str__(self):
        sets = collections.defaultdict(list)
        for child in self.child_to_parent.keys():
            parent = self.find(child)
            sets[parent].append(child)
        return str(sets)

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

        # Can keep record of the group sizes and change the smaller group's parent
        self.child_to_parent[y_parent] = x_parent


if __name__ == "__main__":
    ds = DisjointSet()
    print(ds)

    ds.union(1, 2)
    print(ds)
    ds.union(2, 3)
    print(ds)

    ds.union(6, 5)
    print(ds)
    ds.union(4, 6)
    print(ds)

    ds.union(1, 6)
    print(ds)
