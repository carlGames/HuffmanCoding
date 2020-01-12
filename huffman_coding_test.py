import unittest
from huffman_coding import Node, HuffmanCoding


class HuffmanCodingTest(unittest.TestCase):

    def test_nodes(self):
        test_node_1 = Node("a", 46)
        test_node_2 = Node("b", 36)
        test_node_3 = Node("a", 46)

        self.assertEqual(test_node_1, test_node_3)
        self.assertNotEqual(test_node_1, test_node_2)
        self.assertTrue(test_node_1 > test_node_2)

    def test_freq_dict(self):
        with open("text.txt", "w") as writeable_file:
            writeable_file.write("Hello World! How is it going? My name is Peter and I like to program!\n")

        huffman = HuffmanCoding("text.txt")
        huffman.build_freq_dict()

        self.assertIn(Node("i", 5), huffman.freq_dict)
        self.assertNotIn(Node("x", 0), huffman.freq_dict)


if __name__ == "__main__":
    unittest.main()
