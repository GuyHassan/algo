"""
Write a function height returns the height of a tree. The height is defined to
be the number of levels. The empty tree has height 0, a tree of one node has
height 1, a root node with one or two leaves as children has height 2, and so on
For example: height of tree is 4

                    9
                 /      \
               6         12
              / \       /   \
            3     8   10      15
                 /              \
                7                18

    height = 4

"""
import unittest
from algorithms.tree.bst import count_left_node
from bst import bst

def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))

"""
    The tree is created for testing:

                    9
                 /      \
               6         12
              / \       /   \
            3     8   10      15
                 /              \
                7                18

    count_left_node = 4

"""

class TestSuite(unittest.TestCase):
    def setUp(self):
        count_left_node(self)

    def test_height(self):
        self.assertEqual(4, height(self.tree.root))

if __name__ == '__main__':
    unittest.main()
