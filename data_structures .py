from collections import defaultdict, deque

class Node:
    """Node class for the Tree"""
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree"""
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        """Insert a node to the Tree"""
        if root is None:
            return Node(value)
        if value < root.data:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root

    def inorder(self, root):
        """Inorder traversal of the Tree"""
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        """Preorder traversal of the Tree"""
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        """Postorder traversal of the Tree"""
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')

    def level_order(self, root):
        """Level order traversal of the Tree"""
        if root is None:
            return
        queue = [root]
        while queue:
            current = queue.pop(0)
            print(current.data, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def search(self, root, value):
        """Search for a node in the Tree"""
        if root is None or root.data == value:
            return root
        if value < root.data:
            return self.search(root.left, value)
        return self.search(root.right, value)

    def find_min(self, root):
        """Find the minimum node in the Tree"""
        current = root
        while current.left:
            current = current.left
        return current.data

    def find_max(self, root):
        """Find the maximum node in the Tree"""
        current = root
        while current.right:
            current = current.right
        return current.data

    def height(self, root):
        """Find the height of the Tree"""
        if root is None:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def count_nodes(self, root):
        """Count the number of nodes in the Tree"""
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def delete(self, root, value):
        """Delete a node from the Tree"""
        if root is None:
            return root
        if value < root.data:
            root.left = self.delete(root.left, value)
        elif value > root.data:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
    
            min_val = self.find_min(root.right)
            root.data = min_val
            root.right = self.delete(root.right, min_val)
        return root

class MinHeap:
    """Min-Heap"""
    def __init__(self):
        self.heap = []

    def parent(self, i):
        """Find the parent of a node in the Heap"""
        return (i - 1) // 2

    def left(self, i):
        """Find the left child of a node in the Heap"""
        return 2 * i + 1

    def right(self, i):
        """Find the right child of a node in the Heap"""
        return 2 * i + 2

    def insert(self, key) :
        """Insert a node into the Heap"""
        self.heap.append(key)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def heapify(self, i):
        """Heapify the Heap"""
        smallest = i
        l = self.left(i)
        r = self.right(i)
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def extract_min(self):
        """Extract the minimum node from the Heap"""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    def peek(self):
        """Peek at the minimum node in the Heap"""
        return self.heap[0] if self.heap else None

    def print_heap(self):
        """Print the Heap"""
        print(self.heap)

class MaxHeap:
    """Max-Heap"""
    def __init__(self):
        self.heap = []

    def parent(self, i):
        """Find the parent of a node in the Heap"""
        return (i - 1) // 2

    def left(self, i):
        """Find the left child of a node in the Heap"""
        return 2 * i + 1

    def right(self, i):
        """Find the right child of a node in the Heap"""
        return 2 * i + 2

    def insert(self, key):
        """Insert a node into the Heap"""
        self.heap.append(key)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def heapify(self, i):
        """Heapify the Heap"""
        largest = i
        l = self.left(i)
        r = self.right(i)
        if l < len(self.heap) and self.heap[l] > self.heap[largest]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def extract_max(self):
        """Extract the maximum node from the Heap"""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    def peek(self):
        """Peek at the maximum node in the Heap"""
        return self.heap[0] if self.heap else None

    def print_heap(self):
        """Print the Heap"""
        print(self.heap)

class Graph:
    """Graph"""
    class GraphAdjacencyList:
        """Graph using Adjacency List representation"""
        def __init__(self, directed=False):
            self.graph = defaultdict(list)
            self.directed = directed
            self.vertices = set()
        
        def add_edge(self, u, v, weight=1):
            """Add an edge to the Graph"""
            self.graph[u].append((v, weight))
            self.vertices.add(u)
            self.vertices.add(v)
            
            if not self.directed:
                self.graph[v].append((u, weight))
        
        def add_vertex(self, v):
            """Add a vertex to the Graph"""
            self.vertices.add(v)
            if v not in self.graph:
                self.graph[v] = []
        
        def get_neighbors(self, v):
            """Get the neighbors of a vertex in the Graph"""
            return self.graph[v]
        
        def get_vertices(self):
            """Get the vertices of the Graph"""
            return list(self.vertices)
        
        def has_edge(self, u, v):
            """Check if there is an edge between two vertices in the Graph"""
            return any(neighbor == v for neighbor, _ in self.graph[u])
        
        def display(self):
            """Display the Graph"""
            for vertex in self.vertices:
                neighbors = [f"{neighbor}({weight})" for neighbor, weight in self.graph[vertex]]
                print(f"{vertex}: {neighbors}")

    class GraphAdjacencyMatrix:
        """Graph using Adjacency Matrix representation"""
        def __init__(self, num_vertices, directed=False):
            self.num_vertices = num_vertices
            self.directed = directed
            self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
            self.vertex_map = {}  
            self.reverse_map = {}
            self.next_index = 0
        
        def add_vertex(self, vertex):
            """Add a vertex to the Graph"""
            if vertex not in self.vertex_map and self.next_index < self.num_vertices:
                self.vertex_map[vertex] = self.next_index
                self.reverse_map[self.next_index] = vertex
                self.next_index += 1
        
        def add_edge(self, u, v, weight=1):
            """Add an edge to the Graph"""
            if u not in self.vertex_map:
                self.add_vertex(u)
            if v not in self.vertex_map:
                self.add_vertex(v)
            
            u_idx = self.vertex_map[u]
            v_idx = self.vertex_map[v]
            
            self.matrix[u_idx][v_idx] = weight
            if not self.directed:
                self.matrix[v_idx][u_idx] = weight
        
        def has_edge(self, u, v):
            """Check if there is an edge between two vertices in the Graph"""
            if u not in self.vertex_map or v not in self.vertex_map:
                return False
            return self.matrix[self.vertex_map[u]][self.vertex_map[v]] != 0
        
        def get_weight(self, u, v):
            """Get the weight of an edge between two vertices in the Graph"""
            if not self.has_edge(u, v):
                return 0
            return self.matrix[self.vertex_map[u]][self.vertex_map[v]]

        def get_neighbors(self, v):
            """Get the neighbors of a vertex in the Graph"""
            if v not in self.vertex_map:
                return []
            
            v_idx = self.vertex_map[v]
            neighbors = []
            for j in range(self.next_index):
                if self.matrix[v_idx][j] != 0: 
                    for vertex, idx in self.vertex_map.items():
                        if idx == j:
                            neighbors.append(vertex)
                            break
            return neighbors

        def display(self):
            """Display the Graph"""
            vertices = [self.reverse_map[i] for i in range(self.next_index)]
            print("   ", " ".join(f"{v:3}" for v in vertices))
            for i in range(self.next_index):
                row = " ".join(f"{self.matrix[i][j]:3}" for j in range(self.next_index))
                print(f"{vertices[i]:3}: {row}")

    class GraphTraversal:
        """Graph traversal algorithms: DFS and BFS"""
        @staticmethod
        def dfs_recursive(graph, start, path=None, visited =None):
            """DFS recursive traversal of the Graph"""
            if visited is None:
                visited = set()
            if path is None:
                path = []
            
            visited.add(start)
            path.append(start)
            
            for neighbor, _ in graph.get_neighbors(start):
                if neighbor not in visited:
                    Graph.GraphTraversal.dfs_recursive(graph, neighbor, visited, path)
            
            return path

        @staticmethod
        def dfs_iterative(graph, start):
            """DFS iterative traversal of the Graph"""
            visited = set()
            stack = [start]
            path = []
            
            while stack:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.add(vertex)
                    path.append(vertex)
                    
                    neighbors = [neighbor for neighbor, _ in graph.get_neighbors(vertex)]
                    for neighbor in reversed(neighbors):
                        if neighbor not in visited:
                            stack.append(neighbor)
            return path
        
        @staticmethod
        def bfs(graph, start):
            """BFS traversal of the Graph"""
            visited = set()
            queue = deque([start])
            path = []
            
            visited.add(start)
            
            while queue:
                vertex = queue.popleft()
                path.append(vertex)
                
                for neighbor, _ in graph.get_neighbors(vertex):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return path
