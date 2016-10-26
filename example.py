from file_utils import *
from graph_utils import *

nodes,edge_list,neighbors,weights = read_file('example.txt',False,True)
degree = node_degree(neighbors,nodes)
cc = find_largest_cc(nodes,edge_list,neighbors)
ba = barabasi_albert(10,nodes,edge_list)
er = erdos_renyi(10,15)
