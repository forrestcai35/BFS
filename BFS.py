
import collections


import collections
  
def bfs(graph,root):
    """
    Basic implementation of Bredth First Search
    """
    visited = set()

    queue = collections.dequqe([root])

    #While queue is not empty
    while queue:
        
        #pop the head of the queue 
        vertex = queue.popleft()


        #for each neighbour of the head of the queue 
        for neighbour in graph[vertex]:
            #if the neighbour has not been visited 
            if neighbour not in visited:
                #add neighbour to the visited and queue
                visited.add(neighbour)
                queue.append(neighbour)
graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
print("Following is Breadth First Traversal: ")
bfs(graph, 0)
