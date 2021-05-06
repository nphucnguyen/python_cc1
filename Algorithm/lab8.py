# Tính chiều cao cây tổng quát
class TreeDepth:
    def __init__(self,parents):
        self._parents = parents
        self._n = len(parents)
        self._max_depth = 0
        self._depths = [None] * self._n
    
    def max_depth(self):
        if self._max_depth == 0:
            for idx, parent in enumerate(self._parents):
                depth = self.get_depth(idx)
                if self._max_depth < depth:
                    self._max_depth = depth
        return self._max_depth

        # truy lan tu node cu the den root
    def get_depth (self, idx):
        depth = self._depths[idx]
        if depth is not None:
            return depth
        parent = self._parents[idx]
        if parent == -1:
            depth = 1
        else:
            depth = self.get_depth(parent) +1
        self._depths[idx] = depth
        return depth


tree = TreeDepth([4,-1,4,1,1])
print(tree.max_depth())
print(tree.get_depth(0))
