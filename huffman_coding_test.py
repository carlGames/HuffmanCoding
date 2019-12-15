import unittest
from huffman_coding import Node


class HuffmanCodingTest(unittest.TestCase):

    def test_nodes(self):
        test_node_1 = Node("a", 46)
        test_node_2 = Node("b", 36)
        test_node_3 = Node("a", 46)

        self.assertEqual(test_node_1, test_node_3)
        self.assertNotEqual(test_node_1, test_node_2)


if __name__ == "__main__":
    unittest.main()
