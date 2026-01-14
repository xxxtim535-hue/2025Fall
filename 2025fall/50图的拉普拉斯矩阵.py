m, n = map(int, input().split())
matrix = [[0]*m for _ in range(m)]
for _ in range(n):
    x, y = map(int, input().split())
    matrix[x][y] = -1
    matrix[y][x] = -1

for i in range(m):
    matrix[i][i] = matrix[i].count(-1)

for i in range(m):
    print(" ".join(map(str, matrix[i])))


傻逼


class Vertex:
    """顶点类"""

    def __init__(self, id):
        self.id = id
        self.neighbors = set()  # 存储相邻顶点

    def add_neighbor(self, neighbor_id):
        """添加相邻顶点"""
        self.neighbors.add(neighbor_id)

    def get_degree(self):
        """获取顶点的度（相邻边数）"""
        return len(self.neighbors)


class Graph:
    """图类"""

    def __init__(self, n):
        self.n = n  # 顶点数
        self.vertices = [Vertex(i) for i in range(n)]

    def add_edge(self, a, b):
        """添加无向边"""
        if 0 <= a < self.n and 0 <= b < self.n:
            self.vertices[a].add_neighbor(b)
            self.vertices[b].add_neighbor(a)

    def get_degree_matrix(self):
        """获取度数矩阵D"""
        D = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            D[i][i] = self.vertices[i].get_degree()
        return D

    def get_adjacency_matrix(self):
        """获取邻接矩阵A"""
        A = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in self.vertices[i].neighbors:
                A[i][j] = 1
        return A

    def get_laplacian_matrix(self):
        """获取拉普拉斯矩阵L = D - A"""
        D = self.get_degree_matrix()
        A = self.get_adjacency_matrix()

        L = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                L[i][j] = D[i][j] - A[i][j]
        return L

    def print_laplacian_matrix(self):
        """输出拉普拉斯矩阵"""
        L = self.get_laplacian_matrix()
        for row in L:
            print(" ".join(map(str, row)))


def main():
    # 读取输入
    n, m = map(int, input().split())

    # 创建图
    graph = Graph(n)

    # 添加边
    for _ in range(m):
        a, b = map(int, input().split())
        graph.add_edge(a, b)

    # 输出拉普拉斯矩阵
    graph.print_laplacian_matrix()


if __name__ == "__main__":
    main()

