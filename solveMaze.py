from collections import deque
import timeit

def main(filename):
    """
    O(N): the size of the contents(maze)
    Using online approach
    """
    g = 0
    adj = []
    infile = open(filename,'r')
    contents = infile.read().splitlines()
    tmp = []
    for i in range(len(contents)):
        big = []
        k = 1
        for j in range(len(contents[i])):
            if i == 0:
                if j == 0:#top left corner
                    result = []
                    if contents[i][j] != '#':
                        if contents[i][j] == 'F':#check if finish
                            end = g
                        if contents[i][j] == 'S':#check if start
                            start = g
                        if contents[i][j+1] != '#':
                            result.append(g+1)#right
                        big.append(g)
                        g += 1
                        adj.append(result)
                    else:
                        big.append('#')
                        
                elif j == len(contents[i])-1:
                    result = []
                    if contents[i][j] != '#':
                        if contents[i][j] == 'F':#check if finish
                            end = g
                        if contents[i][j] == 'S':#check if start
                            start = g
                        if contents[i][j-1] != '#':
                            result.append(g-1)#left
                        big.append(g)
                        g += 1
                        adj.append(result)
                    else:
                        big.append('#')
                else:
                    result = []
                    if contents[i][j] != '#':
                        if contents[i][j] == 'F':#check if finish
                            end = g
                        if contents[i][j] == 'S':#check if start
                            start = g
                        if contents[i][j-1] != '#':
                            result.append(g-1)#left
                        if contents[i][j+1] != '#':
                            result.append(g+1)#right
                        big.append(g)
                        g += 1
                        adj.append(result)
                    else:
                        big.append('#')
            
                while k < 2:
                    tmp.append(big)
                    k += 1
                
            
            elif i == len(contents)-1:
                if j == 0:
                    result = []
                    if contents[i][j] != '#':
                        if contents[i][j] == 'F':#check if finish
                            end = g
                        if contents[i][j] == 'S':#check if start
                            start = g
                        if tmp[len(tmp)-1][j] != '#':
                            adj[tmp[len(tmp)-1][j]].append(g)#add current to above row
                            result.append(tmp[len(tmp)-1][j]) #append the above value to current
                        if contents[i][j+1] != '#':
                            result.append(g+1)#right
                        big.append(g)
                        g += 1
                        adj.append(result)
                    else:
                        big.append('#')
                       
                elif j == len(contents[i])-1:
                    result = []
                    if contents[i][j] != '#':
                        if contents[i][j] == 'F':#check if finish
                            end = g
                        if contents[i][j] == 'S':#check if start
                            start = g
                        if tmp[len(tmp)-2][j] != '#':
                            adj[tmp[len(tmp)-2][j]].append(g)#add current to above row
                            result.append(tmp[len(tmp)-2][j]) #append the above value to current 
                        if contents[i][j-1] != '#':
                            result.append(g-1)#left
                        big.append(g)
                        g += 1
                        adj.append(result)
                    else:
                        big.append('#')
                else:
                    result = []
                    if contents[i][j] != '#':
                        if contents[i][j] == 'F':#check if finish
                            end = g
                        if contents[i][j] == 'S':#check if start
                            start = g
                        if tmp[len(tmp)-2][j] != '#':
                            adj[tmp[len(tmp)-2][j]].append(g)#add current to above row
                            result.append(tmp[len(tmp)-2][j])#append the above value to current 
                        if contents[i][j+1] != '#':
                            result.append(g+1)#right
                        if contents[i][j-1] != '#':
                            result.append(g-1)#left
                        big.append(g)
                        g += 1
                        adj.append(result)
                    else:
                        big.append('#')
                        
                while k < 2:
                    tmp.append(big)
                    k += 1
                
            else:
                if j == 0:#first
                    result = []
                    if contents[i][j] != '#':
                        if contents[i][j] == 'F':#check if finish
                            end = g
                        if contents[i][j] == 'S':#check if start
                            start = g
                        if tmp[len(tmp)-1][j] != '#':
                            adj[tmp[len(tmp)-1][j]].append(g)#add current to above row
                            result.append(tmp[len(tmp)-1][j]) #append the above value to current 
                        if contents[i][j+1] != '#':
                            result.append(g+1)#right
                        big.append(g)
                        g += 1
                        adj.append(result)
                    else:
                        big.append('#')
                        
                elif j == len(contents[i])-1:#last
                    result = []
                    if contents[i][j] != '#':
                        if contents[i][j] == 'F':#check if finish
                            end = g
                        if contents[i][j] == 'S':#check if start
                            start = g
                        if tmp[len(tmp)-2][j] != '#':
                            adj[tmp[len(tmp)-2][j]].append(g)#add current to above row
                            result.append(tmp[len(tmp)-2][j]) #append the above value to current 
                        if contents[i][j-1] != '#':
                            result.append(g-1)#right
                        big.append(g)
                        g += 1
                        adj.append(result)
                    else:
                        big.append('#')
                else:
                    result = []
                    if contents[i][j] != '#':
                        if contents[i][j] == 'F':#check if finish
                            end = g
                        if contents[i][j] == 'S':#check if start
                            start = g
                        if tmp[len(tmp)-2][j] != '#':
                            adj[tmp[len(tmp)-2][j]].append(g)#add current to above row
                            result.append(tmp[len(tmp)-2][j]) #append the above value to current
                        if contents[i][j+1] != '#':
                            result.append(g+1)
                        if contents[i][j-1] != '#':
                            result.append(g-1)#right
                        big.append(g)
                        g += 1
                        adj.append(result)
                    else:
                        big.append('#')
                        
                while k < 2:
                    tmp.append(big)
                    k += 1
    infile.close()                
    """
    Complexity: O(|V|+|E|),
    where e is actually the adj
    """
    visited = []
    inqueue = []
    pred = []#denotes the vertex that proceeded u on the shortest path from s
    for i in range(len(adj)):
        visited.append(False)#init first
        inqueue.append(False)#init first
        pred.append(0) 
    queue = deque()
    queue.append(start)#add start
    while len(queue) > 0:#while queue is not empty
        u = queue.popleft()
        visited[u] = True
        inqueue[u] = False
        for i in range(len(adj[u])):
            #result[u][i] = v in here
            if not visited[adj[u][i]] and not inqueue[adj[u][i]]:
                pred[adj[u][i]] = u
                queue.append(adj[u][i])
                inqueue[adj[u][i]] = True
                
    #complexity: O(|V|)
    v = end
    path = [v]
    while pred[v] != 0:
      path.append(pred[v])
      v = pred[v]
    
    return path, tmp, start, end

filename = str(input("Please enter file name: "))
f = open("solution.txt",'w')

start = timeit.default_timer()

path, tmp, s, e = main(filename)
path_set=set(path)

for i in tmp:
    output = ''.join('#' if j=='#'
                    else 'o' if j in path_set or j == e or j == s
                    else '.' 
                for j in i)
    f.write(output+"\n")
    
taken = (timeit.default_timer() - start)
print(taken)    

f.close()



