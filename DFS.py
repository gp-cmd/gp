graph={'A':['B','C','D'],
       'B':['A','D'],
       'C':['A','D','E'],
       'D':['A','B','C'],
       'E':['C','D']}
visited=[]

def dfs(node,visited,graph):
    if node not in visited:
        print(node)
        visited.append(node)
        for i in graph[node]:
            dfs(i,visited,graph)

dfs('A',visited,graph)