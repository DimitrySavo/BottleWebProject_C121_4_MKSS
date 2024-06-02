from bottle import Bottle, run, request, static_file, template, response, route
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
import json

class Graph:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_edge(self, v1, v2):
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1

    # New method to add nodes from a list
    def add_nodes_from(self, nodes):
        new_size = max(nodes) + 1
        if new_size > self.size:
            for row in self.matrix:
                row.extend([0] * (new_size - self.size))
            for _ in range(new_size - self.size):
                self.matrix.append([0] * new_size)
            self.size = new_size

    # New method to add edges from a list
    def add_edges_from(self, edges):
        for v1, v2 in edges:
            self.add_edge(v1, v2)

    def add_nodesAndEdges(self,nodes, edges):
        self.add_nodes_from(range(1, nodes))
        self.add_edges_from( [(edge[0], edge[1]) for edge in edges])

    # Getter method to retrieve nodes
    def get_nodes(self):
        return list(range(self.size))

    # Getter method to retrieve edges
    def get_edges(self):
        edges = []
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.matrix[i][j] == 1:
                    edges.append((i, j))
        return edges

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

    def is_regular(self, amountOfVertexes):
        if self.size == amountOfVertexes:
            degrees = self.degrees()
            first_degree = degrees[0]
            for degree in degrees:
                if degree != first_degree:
                    return "Граф не правильный"
            return "Граф правильный"
        return "Не верное число вершин"
    
    # Новый метод для подсчета числа ребер
    def count_edges(self):
        count = 0
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.matrix[i][j] == 1:
                    count += 1
        return count

    # Новый метод для определения числа изолированных подграфов
    def count_isolated_subgraphs(self):
        visited = [False] * self.size
        count = 0

        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                for neighbor in range(self.size):
                    if self.matrix[current][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

        for i in range(self.size):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1

        return count

    # Новый метод для нахождения диаметра графа
    def diameter(self):
        def bfs(start):
            distances = [-1] * self.size
            distances[start] = 0
            queue = [start]

            while queue:
                current = queue.pop(0)
                for neighbor in range(self.size):
                    if self.matrix[current][neighbor] == 1 and distances[neighbor] == -1:
                        distances[neighbor] = distances[current] + 1
                        queue.append(neighbor)

            return distances

        max_distance = 0
        for i in range(self.size):
            distances = bfs(i)
            max_distance = max(max_distance, max(distances))

        return max_distance
    