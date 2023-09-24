from typing import List
from typing import Dict


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
    treeNode = [HuffmanNode(frequency=frequency, command=command) for command, frequency in
                command_frequencies.items()]

    sort_tree(treeNode)

    while len(treeNode) > 1:
        new_node = HuffmanNode(frequency=sum(node.frequency for node in treeNode[:2]),
                               left=treeNode[0],
                               right=treeNode[1])
        treeNode = treeNode[2:]

        # depends on preferred encoding

        # treeNode.append(new_node)
        treeNode.insert(0, new_node)
        sort_tree(treeNode)

    return treeNode[0]


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
