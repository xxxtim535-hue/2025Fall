from sys用法 import stdin
from collections import defaultdict

def main():
    n = int(stdin.readline())
    children = defaultdict(list)
    parent_map = {}
    node_values = set()

    for _ in range(n):
        data = list(map(int, sys.stdin.readline().split()))
        node = data[0]
        node_values.add(node)

