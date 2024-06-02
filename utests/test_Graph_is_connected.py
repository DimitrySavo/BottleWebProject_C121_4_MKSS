import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Graph import Graph

TRUEGRAPHRORTEST = Graph(4)
TRUEGRAPHRORTEST.add_nodesAndEdges(4,[(0,1),(1,2),(2,3),(1,0),(2,1),(3,2)])

FALSEGRAPHFORTEST = Graph(4)
FALSEGRAPHFORTEST.add_nodesAndEdges(4,[(1,0),(0,1)])

class IsConnectedTests(unittest.TestCase):
    def test_T_is_connected(self):
        self.assertTrue(TRUEGRAPHRORTEST.is_connected())

    def test_F_is_connected(self):
        self.assertFalse(FALSEGRAPHFORTEST.is_connected())

if __name__ == '__main__':
    unittest.main()