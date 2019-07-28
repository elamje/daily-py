class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Test:
    @staticmethod
    def serialize(root):
        if (root == None):
            return '#'
        return '{} {} {}'.format(root.val, Test.serialize(root.left), Test.serialize(root.right))

    @staticmethod
    def deserialize(data):
        def helper():
            val = next(vals)
            if val == '#':
                return None
            node = Node(val)
            node.left = helper()
            node.right = helper()
            return node
        vals = iter(data.split())
        return helper()

    @staticmethod
    def run():
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        assert Test.deserialize(Test.serialize(node)).left.left.val == 'left.left'
