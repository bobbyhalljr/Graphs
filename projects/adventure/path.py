class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def get_neighbors(self, vertex_id):
    """
    Get all neighbors (edges) of a vertex.
    """
    return self.vertices[vertex_id]

def dft(self, starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    # Create an empty stack
    s = Stack()
    # Push the starting vertex_id to the stack
    s.push(starting_vertex)
    # Create an empty set to store visited nodes
    visited = set()
    # While the stack is not empty...
    while s.size() > 0:
        # Pop the first vertex
        v = s.pop()
        # Check if it's been visited
        # If it has not been visited...
        if v not in visited:
            # Mark it as visited
            print(v)
            visited.add(v)
            # Then push all neighbors to the top of the stack
            for neighbor in self.get_neighbors(v):
                s.push(neighbor)