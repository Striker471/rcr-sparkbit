from typing import List
from typing import Dict
import heapq


class RoboticCodeRepresentationGenerator:
    def __init__(self, issued_commands: List[str]):
        self.command_frequencies = calculate_frequencies(issued_commands)
        self.treeNode = create_tree(self.command_frequencies)
        self.rcr_list = create_rcr_list(self.treeNode)

    def get_rcr(self, command: str) -> str:

        if command in self.rcr_list:
            return self.rcr_list[command]
        else:
            return "Command not found"


class HuffmanNode:
    def __init__(self, frequency=0, command=None, left=None, right=None):
        self.frequency = frequency
        self.command = command
        self.left = left
        self.right = right


def sort_tree(treeNode: List[HuffmanNode]):
    return treeNode.sort(key=lambda item: item.frequency)


def calculate_frequencies(issued_commands: List[str]) -> Dict[str, int]:
    command_frequencies = {}
    for command in issued_commands:
        if command in command_frequencies:
            command_frequencies[command] += 1
        else:
            command_frequencies[command] = 1
    return command_frequencies


def create_tree(command_frequencies: Dict[str, int]) -> HuffmanNode:
    priority_queue = [(frequency, HuffmanNode(frequency=frequency, command=command)) for command, frequency in
                      command_frequencies.items()]

    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        freq1, node1 = heapq.heappop(priority_queue)
        freq2, node2 = heapq.heappop(priority_queue)

        new_node = HuffmanNode(frequency=freq1 + freq2,
                               left=node1,
                               right=node2)

        heapq.heappush(priority_queue, (new_node.frequency, new_node))

    return priority_queue[0][1]


def recursive_rcr(node: HuffmanNode, current_code: str, rcr_list: Dict[str, str]):
    if node.command is not None:
        rcr_list[node.command] = current_code
        return

    if node.left is not None:
        recursive_rcr(node.left, current_code + '0', rcr_list)

    if node.right is not None:
        recursive_rcr(node.right, current_code + '1', rcr_list)


def create_rcr_list(treeNode: HuffmanNode) -> Dict[str, str]:
    rcr_list = {}
    recursive_rcr(treeNode, current_code="", rcr_list=rcr_list)
    return rcr_list
