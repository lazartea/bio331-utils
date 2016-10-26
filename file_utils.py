def read_file(filename,undirected,weighted):
    '''
    input: a .txt file containing a graph, whether the graph is directed or undirected, and whether the graph is weighted
    output: list of the graph's nodes, list of edges, dictionary of each node's neighbors, and dictionary of weights (if weighted)
    '''
    openfile = open(filename,'r')
    readfile = openfile.read()

    #splits the file by line
    lines = readfile.split('\n')
   
    edge_list = []
    weight_d = {}
    for item in lines:
        if item != '':
            if weighted == False:
                a,b = item.split('\t')
            else:
                a,b,c = item.split('\t')
            #gets rid of self loops
            if a != b:
                if [a,b] not in edge_list:
                    if undirected == False:
                        edge_list = edge_list + [[a,b]]
                    else:
                        #removes multiple connections
                        if [b,a] not in edge_list:
                            #adds to edge list
                            edge_list = edge_list + [[a,b]]
                #create weight dictionary
                if (a,b) not in weight_d:
                    weight_d[(a,b)] = c
                        
    nodes = []
    #create node list
    for item in edge_list:
        if item[0] not in nodes:
            nodes.append(item[0])
        if item[1] not in nodes:
            nodes.append(item[1])


    #find neighbors                  
    neighbors = {}
    for item in edge_list:
        if undirected: 
            if item[1] not in neighbors:
                neighbors[item[1]] = [item[0]]
            elif neighbors[item[0]] not in neighbors[item[1]]:
                neighbors[item[1]].append(item[0])
            if item[0] not in neighbors:
                neighbors[item[0]] = [item[1]]  
            elif item[1] not in neighbors[item[0]]:
                neighbors[item[0]].append(item[1])
        else:
            if item[0] not in neighbors:
                neighbors[item[0]] = [item[1]]  
            elif item[1] not in neighbors[item[0]]:
                neighbors[item[0]].append(item[1])

    
    if weighted:
        return nodes,edge_list,neighbors,weight_d
    else:
        return nodes,edge_list,neighbors