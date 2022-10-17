"""
A matrix is basically an undirected graph so we can perform a breadth first search or depth first search.
In this solution I will use bfs. We will also store the visited nodes in a set to keep track.

Time Complexity: O(nxn) since we are traversing a matrix of n rows and n columns.
"""

import collections


class Solution:
    def __init__(self, row, col, matrix):
        self.row = row
        self.col = col
        self.matrix = matrix
        self.visit = set()  # create a set to store visited nodes of the graph
        self.visit_zero = set()
        self.count_one = 0  # counter to count group of 1
        self.count_zero = 0  # counter to count group of zero

    def bfs_one(self, r, c):
        q = collections.deque()
        self.visit.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # since we look for adjacents, we can go left, right, up or down.
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(self.row) and
                        c in range(self.col) and  # check if position is in bounds
                        self.matrix[r][c] == 1 and  # check if it is 1
                        (r, c) not in self.visit):
                    q.append((r, c))
                    self.visit.add((r, c))

    def bfs_zero(self, r0, c0):
        q0 = collections.deque()
        self.visit_zero.add((r0, c0))
        q0.append((r0, c0))

        while q0:
            row, col = q0.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # since we look for adjacents.
            for dr0, dc0 in directions:
                r0, c0 = row + dr0, col + dc0
                if (r0 in range(self.row) and
                        c0 in range(self.col) and
                        self.matrix[r0][c0] == 0 and  # check it is 0
                        (r0, c0) not in self.visit_zero):
                    q0.append((r0, c0))
                    self.visit_zero.add((r0, c0))

    def counter(self):
        for r in range(self.row):
            for c in range(self.col):
                if self.matrix[r][c] == 1 and (r, c) not in self.visit:
                    self.bfs_one(r, c)  # run bfs
                    self.count_one += 1

        for r0 in range(self.row):
            for c0 in range(self.col):
                if self.matrix[r0][c0] == 0 and (r0, c0) not in self.visit_zero:
                    self.bfs_zero(r0, c0)  # run bfs
                    self.count_zero += 1

        return self.count_one, self.count_zero


# Outputs

# first example
test_matrix1 = [[1, 0, 1, 1],
         [0, 1, 0, 0],
         [1, 0, 1, 1],
         [1, 0, 0, 0]]

row1 = len(test_matrix1)
col1 = len(test_matrix1[0])
answer1 = Solution(row1, col1, test_matrix1)
print(answer1.counter())

# second example
test_matrix2 = [[0, 0, 1, 1],
         [0, 0, 1, 0],
         [1, 0, 0, 1],
         [1, 1, 1, 0]]

row2 = len(test_matrix2)
col2 = len(test_matrix2[0])
answer2 = Solution(row2, col2, test_matrix2)
print(answer2.counter())

# third example
test_matrix3 = [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 1]]

row3 = len(test_matrix3)
col3 = len(test_matrix3[0])
answer3 = Solution(row3, col3, test_matrix3)
print(answer3.counter())
