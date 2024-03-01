import csv
import io
from collections import defaultdict
from typing import Dict, List, Tuple

def parse_csv(csv_content: str, delimiter=',') -> List[Tuple[int, int]]:
    edge_list = []
    buffer = io.StringIO(csv_content)
    csv_reader = csv.reader(buffer, delimiter=delimiter)
    for line in csv_reader:
        if len(line) == 2:
            edge_list.append((int(line[0]), int(line[1])))
    return edge_list

def construct_graph(edge_list: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    graph = defaultdict(list)
    for start, end in edge_list:
        graph[start].append(end)
    return graph

def dfs(graph: Dict[int, List[int]], node: int, current_depth: int, depths: Dict[int, int]) -> None:
    depths[node] = current_depth
    for neighbor in graph.get(node, []):
        dfs(graph, neighbor, current_depth + 1, depths)

def calculate_subtree_sizes(graph: Dict[int, List[int]], node: int, subtree_sizes: Dict[int, int]) -> int:
    size = 1
    for child in graph.get(node, []):
        size += calculate_subtree_sizes(graph, child, subtree_sizes)
    subtree_sizes[node] = size
    return size

def group_nodes_by_depth(depths: Dict[int, int]) -> Dict[int, List[int]]:
    levels = defaultdict(list)
    for node, depth in depths.items():
        levels[depth].append(node)
    return levels

def task(csv_input: str) -> str:
    edges = parse_csv(csv_input)

    graph = construct_graph(edges)
    reverse_graph = {child: parent for parent, children in graph.items() for child in children}

    num_children = {node: len(children) for node, children in graph.items()}
    depths = {}
    subtree_sizes = {}

    for node in graph:
        if node not in depths:
            dfs(graph, node, 0, depths)
        if node not in subtree_sizes:
            calculate_subtree_sizes(graph, node, subtree_sizes)

    levels = group_nodes_by_depth(depths)

    output_buffer = io.StringIO()
    csv_writer = csv.writer(output_buffer, delimiter=',')

    for node in sorted(graph.keys()):
        r1 = num_children.get(node, 0)
        r2 = 1 if node in reverse_graph else 0
        r3 = subtree_sizes.get(node, 1) - r1 - 1
        r4 = depths.get(node, 0) - 1 if node in reverse_graph else 0
        r5 = len(levels[depths[node]]) - 1
        csv_writer.writerow([r1, r2, r3, r4, r5])

    return output_buffer.getvalue().strip()

def save_csv_data_to_file(csv_data: str, file_path: str) -> None:
    with open(file_path, 'w', newline='') as file:
        file.write(csv_data)

csv_data = "1,2\n1,3\n3,4\n3,5"
csv_output = task(csv_data)

output_file_path = "./task3.csv"
save_csv_data_to_file(csv_output, output_file_path)
