class Graph:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_edge(self, v1, v2):
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1

    def to_dict(self):
        return {
            "size": self.size,
            "matrix": self.matrix
        }

    def path(self, start, end):
        visited = [False] * self.size
        return self.dfs(start, end, visited)

    def dfs(self, current, end, visited):
        if current == end:
            return True
        visited[current] = True
        for neighbor in range(self.size):
            if self.matrix[current][neighbor] == 1 and not visited[neighbor]:
                if self.dfs(neighbor, end, visited):
                    return True
        return False

    def is_connected(self):
        for i in range(1, self.size):
            if not self.path(0, i):
                return False
        return True

    def degrees(self):
        degrees = [0] * self.size
        for i in range(self.size):
            degrees[i] = sum(self.matrix[i])
        return degrees

    def is_regular(self):
        degrees = self.degrees()
        first_degree = degrees[0]
        for degree in degrees:
            if degree != first_degree:
                return False
        return True
