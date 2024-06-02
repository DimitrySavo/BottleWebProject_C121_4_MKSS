import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Graph import Graph

GRAPHRORTEST = Graph(4)
GRAPHRORTEST.add_nodesAndEdges(4,[(0,1),(1,2),(2,3),(1,0),(2,1),(3,2)])


class DfsTests(unittest.TestCase):
    def test_T_dfs_with_0_to_3(self):
        self.assertTrue(GRAPHRORTEST.dfs(0, 3, [False] * 4, 0))
    def test_T_dfs_with_0_to_1(self):
        self.assertTrue(GRAPHRORTEST.dfs(0, 1, [False] * 4, 0))
    def test_T_dfs_with_0_to_2(self):
        self.assertTrue(GRAPHRORTEST.dfs(0, 2, [False] * 4, 0))
    def test_T_dfs_with_1_to_3(self):
        self.assertTrue(GRAPHRORTEST.dfs(1, 3, [False] * 4, 0))