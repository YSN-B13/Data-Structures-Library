from collections import defaultdict

class DS:
    class Node:
        def __init__(self, value):
            self.data = value
            self.left = None
            self.right = None

    """Binary Search Tree"""
    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, root, value):
            if root is None:
                return DS.Node(value)
            if value < root.data:
                root.left = self.insert(root.left, value)
            else:
                root.right = self.insert(root.right, value)
            return root

        def inorder(self, root):
            if root:
                self.inorder(root.left)
                print(root.data, end=' ')
                self.inorder(root.right)

        def preorder(self, root):
            if root:
                print(root.data, end=' ')
                self.preorder(root.left)
                self.preorder(root.right)

        def postorder(self, root):
            if root:
                self.postorder(root.left)
                self.postorder(root.right)
                print(root.data, end=' ')

        def level_order(self, root):
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
            if root is None or root.data == value:
                return root
            if value < root.data:
                return self.search(root.left, value)
            return self.search(root.right, value)

        def find_min(self, root):
            current = root
            while current.left:
                current = current.left
            return current.data

        def find_max(self, root):
            current = root
            while current.right:
                current = current.right
            return current.data

        def height(self, root):
            if root is None:
                return -1
            return 1 + max(self.height(root.left), self.height(root.right))

        def count_nodes(self, root):
            if root is None:
                return 0
            return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

        def delete(self, root, value):
            if root is None:
                return root
            if value < root.data:
                root.left = self.delete(root.left, value)
            elif value > root.data:
                root.right = self.delete(root.right, value)
            else:
                # Node with only one child or no child
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                # Node with two children:
                # Get inorder successor (smallest in the right subtree)
                min_val = self.find_min(root.right)
                root.data = min_val
                root.right = self.delete(root.right, min_val)
            return root

    """ Min-Heap"""
    class MinHeap:
        def __init__(self):
            self.heap = []

        def parent(self, i):
            return (i - 1) // 2

        def left(self, i):
            return 2 * i + 1

        def right(self, i):
            return 2 * i + 2

        def insert(self, key) :
            self.heap.append(key)
            i = len(self.heap) - 1
            while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
                self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
                i = self.parent(i)

        def heapify(self, i):
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
            if len(self.heap) == 0:
                return None
            if len(self.heap) == 1:
                return self.heap.pop()
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify(0)
            return root

        def peek(self):
            return self.heap[0] if self.heap else None

        def print_heap(self):
            print(self.heap)

    """Max-Heap"""
    class MaxHeap:
        def __init__(self):
            self.heap = []

        def parent(self, i):
            return (i - 1) // 2

        def left(self, i):
            return 2 * i + 1

        def right(self, i):
            return 2 * i + 2

        def insert(self, key):
            self.heap.append(key)
            i = len(self.heap) - 1
            while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
                self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
                i = self.parent(i)

        def heapify(self, i):
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
            if len(self.heap) == 0:
                return None
            if len(self.heap) == 1:
                return self.heap.pop()
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify(0)
            return root

        def peek(self):
            return self.heap[0] if self.heap else None

        def print_heap(self):
            print(self.heap)

    """Graphs"""
    class Graph:
        class GraphAdjacencyList:
            def __init__(self, directed=False):
                self.graph = defaultdict(list)
                self.directed = directed
                self.vertices = set()
            
            def add_edge(self, u, v, weight=1):
                self.graph[u].append((v, weight))
                self.vertices.add(u)
                self.vertices.add(v)
                
                if not self.directed:
                    self.graph[v].append((u, weight))
            
            def add_vertex(self, v):
                self.vertices.add(v)
                if v not in self.graph:
                    self.graph[v] = []
            
            def get_neighbors(self, v):
                return self.graph[v]
            
            def get_vertices(self):
                return list(self.vertices)
            
            def has_edge(self, u, v):
                return any(neighbor == v for neighbor, _ in self.graph[u])
            
            def display(self):
                for vertex in self.vertices:
                    neighbors = [f"{neighbor}({weight})" for neighbor, weight in self.graph[vertex]]
                    print(f"{vertex}: {neighbors}")

        class GraphAdjacencyMatrix:
            def __init__(self, num_vertices, directed=False):
                self.num_vertices = num_vertices
                self.directed = directed
                self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
                self.vertex_map = {}  
                self.reverse_map = {}
                self.next_index = 0
            
            def add_vertex(self, vertex):
                if vertex not in self.vertex_map and self.next_index < self.num_vertices:
                    self.vertex_map[vertex] = self.next_index
                    self.reverse_map[self.next_index] = vertex
                    self.next_index += 1
            
            def add_edge(self, u, v, weight=1):
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
                if u not in self.vertex_map or v not in self.vertex_map:
                    return False
                return self.matrix[self.vertex_map[u]][self.vertex_map[v]] != 0
            
            def get_weight(self, u, v):
                if not self.has_edge(u, v):
                    return 0
                return self.matrix[self.vertex_map[u]][self.vertex_map[v]]

            def get_neighbors(self, v):
                pass

            def display(self):
                pass