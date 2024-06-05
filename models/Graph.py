from bottle import Bottle, run, request, static_file, template, response, route
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
import json
import os

#нахождение делителей
def find_divisors(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return divisors

#построение строки для большой строки из маленьикх матриц
def line_for_big_matrix(size, step, line_part):
    line = [0] * size
    line[step:step + len(line_part)] = line_part
    return line

#Вставка маленьких матриц в большую и после в список матриц
def insert_in_matrix(matrix_list, small_matrix):
    step = len(small_matrix[0])
    big_matrix = [[0 for _ in range(len(matrix_list[0][0]))] for _ in range(len(matrix_list[0][0]))]
    for i in range(len(big_matrix)):
        big_matrix[i] = line_for_big_matrix(len(matrix_list[0][0]), step * (i//len(small_matrix)), small_matrix[i % len(small_matrix)])

    matrix_list.append(big_matrix)
    return matrix_list

#построение строки матрицы для матриц
def generate_matrix_line(amount, size, start_index):
    l = [0] * size
    for i in range(amount):
        l[(1 + start_index + i)% size] = 1
    for i in range(amount):
        l[(size - 1 + start_index - i) % size] = 1
    return l

#генерация всех возможных правильных связных графов
def generate_matrix(size):
    all_matrix = []
    if type(size) != int:
        return all_matrix
    if size == 1:
        all_matrix.append([1])
        return all_matrix
    m = []
    for i in range(size):
        for j in range(size):
            m.append(generate_matrix_line(i, size, j))
        all_matrix.append(m)
        if sum(m[0]) == size - 1:
            print(f"Found a solution at iteration {i}")
            break
        m = []

    return all_matrix


def add_incoherenet_graphs(matrix_list, size):
    if size % 2 == 0:
        for div in find_divisors(size):
            if div == 1 or div == size:
                continue
            list_of_small_matrixes = generate_matrix(div)
            for small_matrix in list_of_small_matrixes:
                matrix_list = insert_in_matrix(matrix_list, small_matrix)
    return matrix_list  
        

def call_both(size):
    matrix_list = generate_matrix(size)
    matrix_list = add_incoherenet_graphs(matrix_list, size)
    return matrix_list

class Graph:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_edge(self, v1, v2):
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1

    # add nodes from a list
    def add_nodes_from(self, nodes):
        new_size = max(nodes) + 1
        if new_size > self.size:
            for row in self.matrix:
                row.extend([0] * (new_size - self.size))
            for _ in range(new_size - self.size):
                self.matrix.append([0] * new_size)
            self.size = new_size

    # add edges from a list
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
            for j in range(self.size):
                if self.matrix[i][j] == 1:
                    edges.append([i, j])
        return edges

    def to_dict(self):
        return {
            "size": self.size,
            "matrix": self.matrix
        }

    def path(self, start, end):
        visited = [False] * self.size
        return self.dfs(start, end, visited, 0)

    #Алгоритм поиска в глубину
    def dfs(self, current, end, visited, nested_count):
        if current == end:
            if self.matrix[current][end] == 1 and nested_count == 0: #Проверка на петлю
                return True
            elif nested_count > 0:
                return True
        nested_count += 1
        visited[current] = True #Вершина посещена
        for neighbor in range(self.size): #переход на соседнии вершины
            if self.matrix[current][neighbor] == 1 and not visited[neighbor]:
                if self.dfs(neighbor, end, visited, nested_count):
                    return True
        return False 

    #Алгоритм проверяет является ли граф связным
    def is_connected(self):
        for i in range(1, self.size):#Пробегается по всем вершинам графа
            if not self.path(0, i):#И проверяет есть ли такой путь
                return False
        return True

    #Метод для подсчета степеней вершин у графа
    def degrees(self):
        degrees = [0] * self.size
        for i in range(self.size):
            for j in range(self.size):
                if i == j and self.matrix[i][j] == 1: # степень +2 если это вершина
                    degrees[i] += 2
                elif self.matrix[i][j] == 1: # 
                    degrees[i] += 1
        return degrees
    
    

    #Метод для получения правильных графов с заданным количеством вершин
    def is_regular(self, amountOfVertexes):
        list_of_matrix = generate_matrix(amountOfVertexes)

        if amountOfVertexes != 1:
            # Проверяем каждую матрицу на наличие только нулей
            non_empty_matrices = [matrix for matrix in list_of_matrix if any(any(row) for row in matrix)]

            # Преобразование списка матриц в set кортежей
            set_of_matrix = set(tuple(tuple(row) for row in matrix) for matrix in non_empty_matrices)
            return set_of_matrix
        else: 
            return list_of_matrix
            
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
    
    def save_base64_img(self, text):
        history_file = os.path.join('history', 'history.txt')
        try:
            with open(history_file, 'a') as file:  # Открытие файла в режиме добавления
                file.write(text + '\n')  # Запись строки и добавление новой строки
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    @staticmethod
    def union(graph1, graph2): #Метод для поиска объединения графов
        if graph1.size != graph2.size: #Размер графов должен совпадать
            raise ValueError("Graphs must be of the same size to perform union")
        new_graph = Graph(graph1.size)
        for i in range(graph1.size):
            for j in range(graph1.size): #Цикл в котором происходит формирование нового графа
                if graph1.matrix[i][j] == 1 or graph2.matrix[i][j] == 1:
                    new_graph.matrix[i][j] = 1
        return new_graph

    @staticmethod
    def intersection(graph1, graph2): #Метод для поиска пересечения
        if graph1.size != graph2.size: #Размер графов должен совпадать
            raise ValueError("Graphs must be of the same size to perform intersection")
        new_graph = Graph(graph1.size)
        for i in range(graph1.size):
            for j in range(graph1.size): #Цикл в котором происходит формирование нового графа
                if graph1.matrix[i][j] == 1 and graph2.matrix[i][j] == 1:
                    new_graph.matrix[i][j] = 1
        return new_graph

    @staticmethod
    def complement(graph): #Метод для поиска дополнения
        new_graph = Graph(graph.size)
        for i in range(graph.size):
            for j in range(graph.size): 
                if graph.matrix[i][j] == 0:
                    new_graph.matrix[i][j] = 1
                if graph.matrix[i][j] == 1:
                    new_graph.matrix[i][j] = 0
        return new_graph
    
