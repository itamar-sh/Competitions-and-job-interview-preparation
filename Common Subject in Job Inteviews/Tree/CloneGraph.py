class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        def _cloneGraphRecursion(node: 'Node', eqNode: 'Node', neighborsToNode: dict = {}):
            neighborsToNode[node] = eqNode
            next_level = []
            for neighbor in node.neighbors:
                if neighbor not in neighborsToNode:
                    newNode = Node(neighbor.val)
                    neighborsToNode[neighbor] = newNode
                    eqNode.neighbors.append(newNode)
                    next_level.append((neighbor, newNode))
                else:
                    eqNode.neighbors.append(neighborsToNode[neighbor])
            for nodes in next_level:
                _cloneGraphRecursion(nodes[0], nodes[1], neighborsToNode)
            return eqNode

        if node is None:
            return None
        return _cloneGraphRecursion(node, Node(node.val))
