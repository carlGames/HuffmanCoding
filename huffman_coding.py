from __future__ import annotations
from typing import Dict, List, Tuple

class Node:

    def __init__(self: Node, char: str, freq: int) -> None:
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __eq__(self : Node, other: Node) -> bool: 
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
        
    @staticmethod
    def __check(other: Node) -> bool:
        return other is not None and isinstance(other, Node)


def main():
    pass


if __name__ == '__main__':
    main()