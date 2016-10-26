import random 
def erdos_renyi(n,m):
    '''
    Input: the number of nodes and edges
    Output: a graph consisting of n nodes and m edges
    '''
    #from lab2
    nodes = range(1,n+1)
    edges = []
    while len(edges) != m:
        #only adds edges until edges == m
        u = random.choice(nodes)
        v = random.choice(nodes)
        if u != v:
            if [u,v] not in edges:
                if [v,u] not in edges:
                    edges.append([u,v])
                    #only appends edges that aren't already in the list/no self loops/directed edges
    d = {}
    #creates a dictionary of edges
    for item in edges:
        if item[0] not in d:
            d[item[0]] = [item[1]]
            
        elif item[1] not in d[item[0]]:
            d[item[0]].append(item[1])

        if item[1] not in d:
            d[item[1]] = [item[0]]
        elif d[item[0]] not in d[item[1]]:
            d[item[1]].append(item[0])

    return nodes,edges,d

def BFS(nodes,edges,d,s):
    '''
    Input: a graph (list of edges and nodes), a dictionary, and a node of interest
    Output: a list of all visited nodes 
    '''
    Q = [s]
    visited = []
    
    while len(Q) != 0:
        x = Q.pop(0)
        #removes first item in Q
        for item in d[x]:
            if item not in visited:
                #adds item to visited
                visited.append(item)
                #adds item to q
                Q = Q + [item]
    
    return visited



def barabasi_albert(t,V,E):
    #from lab 2
    '''
    Input: a time, a list of nodes, and a list of edges
    Output: a randomly created graph that is built off of the initial graph
    '''
    listofedge = []
    for edge in E:
        listofedge.append(edge[0])
        listofedge.append(edge[1])
    #creates a list of nodes
    while t != 0:
        n = random.choice(listofedge)
        t = t - 1
        new_node = (len(V)+1)
        #adds randomly generated node to list
        V.append(new_node)
        if [n,new_node] not in E:
            #adds randomly generated edge to list
            E.append([new_node,n])
            listofedge.append(new_node)
            listofedge.append(n)
    d = {}
    for item in E:
        if item[0] not in d:
            d[item[0]] = [item[1]]
            
        elif item[1] not in d[item[0]]:
            d[item[0]].append(item[1])

        if item[1] not in d:
            d[item[1]] = [item[0]]
        elif d[item[0]] not in d[item[1]]:
            d[item[1]].append(item[0])

    return V, E, d

def node_degree(d,nodes):
    '''
    Input: a dictionary of neighbors and a list of nodes
    Output: list of all node degrees, list of probablilties for each degree, list of average neighbor degrees
    '''
    deg_num = 0
    list_of_degrees = []
    #I had an issue with selfloops being in my list of nodes but not my dictionary, so I just
    #used the keys 
    for key in d:
        if len(d[key]) not in list_of_degrees:
            #make a list of all possible degrees
            list_of_degrees = list_of_degrees + [len(d[key])]
    #sort the list numerically
    list_of_degrees = sorted(list_of_degrees)

    list_of_probs = []
    for item in list_of_degrees:
        deg_num = 0
        for key in d:
            if len(d[key]) == item:
                deg_num += 1
                #find counts for each degree
                
        #calculate probablilty of each degree
        probability = (deg_num / float(len(nodes)))
        
        
        list_of_probs = list_of_probs + [probability]

    prob_dict = {}
    for item in range(len(list_of_degrees)):
        prob_dict[list_of_degrees[item]] = list_of_probs[item]

    sumofdegree = 0 
    neighbordegree = []
    neighbordegreestat = []
    degreenum = []
    for key in d: 
        for item in d[key]:
            #finds the average neighbor degree for each node

            sumofdegree = len(d[item])
            neighbordegree = [(1.0/len(d[key])) * sumofdegree]
        neighbordegreestat = neighbordegreestat + neighbordegree
        degreenum = degreenum + [len(d[key])]

    #print list_of_degrees,list_of_probs
    return list_of_degrees,list_of_probs,neighbordegreestat,degreenum

def BFS_distance(edges,nodes,s):
    '''
    Input: a graph and node of interest
    Output: dictionary of pathlengths
    '''
    #from lab3

    dist = {}
    dist[s] = 0
    Q = [s]
    visited = []
    max_dist = 0
    neighbors = []
    while len(Q) != 0:
        x = Q.pop(0)
        for e in edges: 
            if e[0] == x:
                neighbors = neighbors + [e[1]]
        for item in neighbors:
            if item not in visited:
                visited.append(item)
                Q = Q + [item]
                dist[item] = dist[x] + 1.0
            if dist[item] > max_dist:
                max_dist = dist[item]
    
    for item in dist:
        dist[item] = (dist[item]+2)/(max_dist+2)
    
    return dist

def find_largest_cc(nodes,edges,d):
    '''
    Input: a graph
    Output: the largest connected component in the graph
    '''
    orig = []
    nodes_visited_list = []
      
    for s in d.keys():
        if s not in nodes_visited_list:
            cc = BFS(nodes,edges,d,s)
            
            if len(orig) < len(cc):
                orig = cc
            nodes_visited_list = nodes_visited_list + cc
    nodelist = []
    for node in orig:
        if node not in nodelist:
            nodelist = nodelist + [node]
    e_list = []
    for node in nodelist:
        for item in edges:
            if node in item:
                a = item[0]
                b = item[1]
                if [b,a] not in e_list and [a,b] not in e_list:
                    e_list = e_list + [item] 

    return orig 

