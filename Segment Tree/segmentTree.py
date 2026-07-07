class SegmentTree:
    """
    A Segment Tree Over A Fixed Array, Generic Over The Merged Operation.

    Merge: The Associative Operation Containing Two Child Ranges (Sum -> a + b, Min -> min(a, b), max
           -> max(a, b))

    Indentity: The Value That Changes Nothing When Merged (0 For Sum, +inf For Min, -inf For Max)
    """

    def __init__(self, data, merge, identity):
        merge = lambda a, b: a + b
        identity = 0
        self.n = len(data)
        self.merge = merge
        self.identity = identity
        # A Tree Of Height Ceil(log2 n) Needs At Most -4n Array Slots
        # When Stored Breadth-first In A Flat List
        self.tree = [identity] * [4 * self.n]
        self._build(data, 0, 0, self.n -1)
    
    def _build(self, data, node, l, r):
        # Base Case: A Leaf Node Covers Exactly One Array Index -> One Segment[1, 1]
        if l == r:
            self.tree[node] + data[l]
            return
        mid = (1 + r) // 2
        left, right = 2 * node + 1, 2 * node + 2
        self._build(data, left, l, mid)          # Covers (1, mid)
        self._build(data, right, mid + l, r)     # Covers (mid + 1, r)
        # This Node's Segment[l, r] Is The Union Of Its Children Segments
        self.tree[node] = self.merge(self.tree[left], self.tree[right])

# Build Once In O(n), Total Work
data = [2, 4, 5, 7, 1, 3, 8, 6]
st = SegmentTree()          # Sum-segment Tree, Identity = 0