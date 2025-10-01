# Data Structures Library

A comprehensive Python library implementing common data structures including Binary Search Trees, Heaps, and Graphs.

## Table of Contents

- [Installation](#installation)
- [Data Structures](#data-structures)
  - [Binary Search Tree](#binary-search-tree)
  - [Min Heap](#min-heap)
  - [Max Heap](#max-heap)
  - [Graph](#graph)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)

## Installation

Simply import the required classes from the module:

```python
from data_structures import BinarySearchTree, MinHeap, MaxHeap, Graph
```

## Data Structures

### Binary Search Tree

A binary search tree implementation with common operations.

**Features:**
- Insert, search, and delete nodes
- Multiple traversal methods (inorder, preorder, postorder, level-order)
- Find minimum and maximum values
- Calculate tree height and node count

**Example:**
```python
bst = BinarySearchTree()
bst.root = bst.insert(bst.root, 50)
bst.root = bst.insert(bst.root, 30)
bst.root = bst.insert(bst.root, 70)

print("Inorder traversal:")
bst.inorder(bst.root)  # Output: 30 50 70
```

### Min Heap

A min-heap implementation where the parent node is always smaller than its children.

**Features:**
- Insert elements while maintaining heap property
- Extract minimum element
- Peek at minimum element without removing it
- Heapify operation

**Example:**
```python
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)

print(min_heap.extract_min())  # Output: 5
print(min_heap.peek())         # Output: 10
```

### Max Heap

A max-heap implementation where the parent node is always larger than its children.

**Features:**
- Insert elements while maintaining heap property
- Extract maximum element
- Peek at maximum element without removing it
- Heapify operation

**Example:**
```python
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(20)

print(max_heap.extract_max())  # Output: 20
print(max_heap.peek())         # Output: 10
```

### Graph

Graph implementations with two representations: Adjacency List and Adjacency Matrix.

#### Graph.GraphAdjacencyList

Efficient for sparse graphs, supports both directed and undirected graphs with weighted edges.

**Features:**
- Add vertices and edges
- Get neighbors of a vertex
- Check edge existence
- DFS and BFS traversal algorithms

**Example:**
```python
graph = Graph.GraphAdjacencyList(directed=False)
graph.add_edge('A', 'B', weight=5)
graph.add_edge('B', 'C', weight=3)
graph.add_edge('A', 'C', weight=7)

graph.display()
# Output:
# A: ['B(5)', 'C(7)']
# B: ['A(5)', 'C(3)']
# C: ['B(3)', 'A(7)']
```

#### Graph.GraphAdjacencyMatrix

Efficient for dense graphs, uses a 2D matrix representation.

**Features:**
- Add vertices and edges
- Check edge existence
- Get edge weights
- Get neighbors of a vertex

**Example:**
```python
graph = Graph.GraphAdjacencyMatrix(num_vertices=5, directed=False)
graph.add_edge('A', 'B', weight=5)
graph.add_edge('B', 'C', weight=3)

print(graph.has_edge('A', 'B'))  # Output: True
print(graph.get_weight('A', 'B'))  # Output: 5
```

#### Graph.GraphTraversal

Static methods for traversing graphs.

**Available Methods:**
- `dfs_recursive()`: Depth-first search using recursion
- `dfs_iterative()`: Depth-first search using a stack
- `bfs()`: Breadth-first search using a queue

**Example:**
```python
graph = Graph.GraphAdjacencyList(directed=False)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')

# DFS traversal
path = Graph.GraphTraversal.dfs_recursive(graph, 'A')
print(path)  # Output: ['A', 'B', 'D', 'C']

# BFS traversal
path = Graph.GraphTraversal.bfs(graph, 'A')
print(path)  # Output: ['A', 'B', 'C', 'D']
```

## Usage Examples

### Complete Binary Search Tree Example

```python
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.root = bst.insert(bst.root, value)

print("Tree height:", bst.height(bst.root))
print("Node count:", bst.count_nodes(bst.root))
print("Min value:", bst.find_min(bst.root))
print("Max value:", bst.find_max(bst.root))

# Delete a node
bst.root = bst.delete(bst.root, 30)
```

### Complete Graph Example with Traversal

```python
# Create a graph
graph = Graph.GraphAdjacencyList(directed=False)
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E')]

for u, v in edges:
    graph.add_edge(u, v)

# Traverse the graph
print("DFS (Recursive):", Graph.GraphTraversal.dfs_recursive(graph, 'A'))
print("DFS (Iterative):", Graph.GraphTraversal.dfs_iterative(graph, 'A'))
print("BFS:", Graph.GraphTraversal.bfs(graph, 'A'))
```

## API Reference

### BinarySearchTree Methods

| Method | Description | Time Complexity |
|--------|-------------|-----------------|
| `insert(root, value)` | Insert a node | O(log n) average |
| `search(root, value)` | Search for a node | O(log n) average |
| `delete(root, value)` | Delete a node | O(log n) average |
| `inorder(root)` | Inorder traversal | O(n) |
| `preorder(root)` | Preorder traversal | O(n) |
| `postorder(root)` | Postorder traversal | O(n) |
| `level_order(root)` | Level-order traversal | O(n) |
| `height(root)` | Get tree height | O(n) |
| `count_nodes(root)` | Count nodes | O(n) |

### Heap Methods

| Method | Description | Time Complexity |
|--------|-------------|-----------------|
| `insert(key)` | Insert element | O(log n) |
| `extract_min/max()` | Remove root element | O(log n) |
| `peek()` | View root element | O(1) |
| `heapify(i)` | Maintain heap property | O(log n) |

### Graph Methods

| Method | Description | Time Complexity |
|--------|-------------|-----------------|
| `add_edge(u, v, weight)` | Add an edge | O(1) for adjacency list |
| `add_vertex(v)` | Add a vertex | O(1) |
| `get_neighbors(v)` | Get adjacent vertices | O(1) for adjacency list |
| `has_edge(u, v)` | Check edge existence | O(1) for matrix, O(degree) for list |
| `dfs()` | Depth-first search | O(V + E) |
| `bfs()` | Breadth-first search | O(V + E) |

## Contributing

This library is designed to be extensible. Future additions may include:
- AVL Trees
- Red-Black Trees
- Trie
- Disjoint Set (Union-Find)
- Priority Queue
- Additional graph algorithms (Dijkstra, Bellman-Ford, Kruskal, Prim)

Feel free to contribute by adding new data structures or improving existing implementations!

## License

This project is open source and available for educational purposes.

---

**Note:** All traversal methods that print output use `print()` with `end=' '` to display elements in a single line separated by spaces.