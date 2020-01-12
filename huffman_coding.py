from __future__ import annotations
from typing import Dict, List, Tuple, Union

class Node:

    def __init__(self: Node, char: str, freq: int) -> None:
        self.char: str = char
        self.freq: int = freq
        self.left: Node = None
        self.right: Node = None

    def __eq__(self: Node, other: Node) -> bool: 
        return Node.__check(other) and \
               self.char == other.char and \
               self.freq == other.freq

    def __lt__(self: Node, other: Node) -> bool:
        return Node.__check(other) and \
               self.freq < other.freq

    def __gt__(self: Node, other: Node) -> bool:
        return Node.__check(other) and \
               self.freq > other.freq

    def __le__(self: Node, other: Node) -> bool:
        return Node.__check(other) and \
               self.freq <= other.freq

    def __ge__(self: Node, other: Node) -> bool:
        return Node.__check(other) and \
               self.freq >= other.freq

    def __str__(self: Node) -> str:
        return "Node('{}', {})".format(self.char, self.freq)

    def increment(self: None) -> None:
        self.freq += 1
        
    @staticmethod
    def __check(other: Node) -> bool:
        return other is not None and isinstance(other, Node)


class HuffmanCoding:

    def __init__(self: HuffmanCoding, path: str) -> None:
        self.path = path
        self.freq_dict = []
        self.node_tree = None

    def load_file(self: HuffmanCoding) -> str:
        with open(self.path, "r") as readable_file:
            return readable_file.read()

    def build_freq_dict(self: HuffmanCoding) -> None:
        text = self.load_file()
        for i in range(len(text)):
            for j in range(len(self.freq_dict)):
                if text[i] == self.freq_dict[j].char:
                    self.freq_dict[j].increment()
                    break
            else:
                self.freq_dict.append(Node(text[i], 1))
        
        self.freq_dict = sorted(self.freq_dict, key=lambda n: n.freq)

    def print_freq_dict(self: HuffmanCoding) -> str:
        result = "["
        for node in self.freq_dict:
            result += str(node) + ", "
        return result[:-1] + "]"

    def build_node_tree(self: HuffmanCoding) -> None:
        self.build_freq_dict()
        queue = self.freq_dict

        while len(queue) != 1:
            left_branch = queue.pop(0)
            right_branch = queue.pop(0)

            tree = Node("Tree", left_branch.freq + right_branch.freq)

            tree.left = left_branch
            tree.right = right_branch

            queue.append(tree)

            queue = sorted(queue, key=lambda n: n.freq)

        self.node_tree = queue

    def build_code_table(self: HuffmanCoding) -> Dict[str, int]:
        pass

    def compress(self: HuffmanCoding) -> str:
        text = self.load_file()

        result = ""

    def decompress(self: HuffmanCoding, code: str) -> str:
        pass


def main():
    pass


if __name__ == '__main__':
    main()