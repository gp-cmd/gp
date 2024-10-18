visited=[]
queue=[]
graph={'A':['B','C','D'],
       'B':['A','D'],
       'C':['A','D','E'],
       'D':['A','B','C'],
       'E':['C','D']}

def bfs(node,visited,graph):
    if node in graph:
        visited.append(node)
        queue.append(node)
        while queue:
            m=queue.pop(0)
            print(" ",m)
            for i in graph[m]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)

bfs('A',visited,graph)