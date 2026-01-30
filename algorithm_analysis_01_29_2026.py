"""
01/29/2026 COMP215 Lecture's Topic - Time Complexity of Algorithms

When comparing the efficiency of an algorithm, we often consider its
time complexity and space complexity, usually focusing on the worst-case scenario.

Time complexity is a function that describes 
how long an algorithm takes in terms of the input size.

Space complexity is a function that describes 
how much memory (space) an algorithm requires to the input size.

Big O notation represents the “order of magnitude” of a function's growth 
as the input size becomes large.
It shows how the running time or space of an algorithm grows relative to the input size n,
ignoring constant factors and lower-order terms. 
E.g., if an algorithm takes f(n) = 3n^2 + 5n + 10 steps, its time complexity big O is O(n^2). 
We ignore lower-order terms 5n + 10, because for large n, the n^2 term dominates. 
We also ignore the constant coefficient 3, leaving the Big O as O(n²).

Assuming the quantity of input is n,
Common time complexities: O(1), O(log n), O(n), O(nlog n), O(n^2), O(2^n), etc.
Common space complexities: O(1), O(n), O(n^2), etc.

Today our focus is on time complexity of algorithms.
"""


#### Constant Time O(1): 
# O(1) means the running time does not depend on the input size.
def sum_nums(a, b):
    return a + b

assert sum_nums(4, 5) == 9
assert sum_nums(0, -1) == -1



def first_item(nums): 
    """Return the first item of a list, or None if the list is empty."""
    if not nums: # if (len(nums) == 0):
        return None
    return nums[0]

assert(first_item([3, 2, 4]) == 3)
assert(first_item([]) == None)



#### Linear Time O(n):
# The running time grows at a linear function of n (proportional to n), where n is the size of input nums

def sum_all_items(nums):
    total = 0
    for num in nums:
        total += num
    return total

assert sum_all_items([3, 2, 4]) == 9
assert sum_all_items([3]) == 3 
assert sum_all_items([]) == 0



def create_list(n):
    a_list = []
    for i in range(n):
        a_list.append(i)
    return a_list
assert create_list(3) == [0, 1, 2]
assert create_list(1) == [0]



def linear_search(nums, target):
    nums_length = len(nums)
    for i in range(nums_length):
        if nums[i] == target:
            return i
    return -1
assert linear_search([1, 5, 8, 10], 8) == 2
assert linear_search([1, 5, 8, 10], 4) == -1


#### Quadratic Time O(n^2):
# The running time grows at a quadratic function of n, where n is the size of input nums

def create_matrix(n):
    a_matrix = []
    for i in range(n):
        a_matrix.append([])
        for j in range(n):
            a_matrix[i].append(j)
    return a_matrix

assert create_matrix(2) == [[0, 1], [0, 1]]
assert create_matrix(1) == [[0]]
assert create_matrix(0) == []



def all_pairs(n): 
    for i in range(n):
        for j in range(i): 
            yield j, i

assert (list(all_pairs(3)) == [(0, 1), (0, 2), (1, 2)]) # 0 + 1 + 2
assert (list(all_pairs(1)) == [])
assert (list(all_pairs(0)) == [])




#### Logarithmic time O(logn) - Highly efficient!

def binary_search(nums, target):
    '''Perform binary search on a sorted list to find the index of a target value.'''
    left = 0  # First index
    right = len(nums) - 1  # Last index
    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    return -1

assert binary_search([1, 5, 8, 10], 8) == 2
assert binary_search([1, 5, 8, 10], 4) == -1



"""
Now let's analyze DFS together!
"""

### DFS time complexity

def is_connected(g, start):
    if start not in g:
        return False  # start node not in graph

    seen = set()
    stack = [start] # BFS deque([start]) # from collections import deque
    while stack: # Keeps track of nodes discovered but not yet processed
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            stack.extend(g.neighbors(node))
    return len(seen) == len(g)

'''
Assume the graph has n nodes/vertices and m edges.

The algorithm visits each node at most once, 
so the cost of adding nodes to seen is O(n).

For each visited vertex, the algorithm iterates over all its neighbors.
Over the entire execution, each edge is examined at most twice 
(once from each endpoint in an undirected graph), 
so the cost of scanning adjacency lists (stack push/pop) is O(m).

Therefore, the total time complexity is O(n + m).
In the special case of a complete graph, where m = n * (n - 1) / 2, 
the time complexity becomes O(n^2).
'''

# Tests for is_connected function
import networkx as nx
n = 3
complete_g = nx.Graph()
complete_g.add_nodes_from(range(n))
complete_g.add_edges_from(all_pairs(n))
assert is_connected(complete_g, 0) == True
assert is_connected(complete_g, 1) == True
assert is_connected(complete_g, 3) == False

disconnected_g = nx.Graph()
disconnected_g.add_nodes_from([0, 1, 2, 3])
disconnected_g.add_edges_from([(0, 1), (1, 2)])
assert is_connected(disconnected_g, 0) == False
