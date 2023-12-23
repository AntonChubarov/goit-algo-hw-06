import networkx as nx

gml_file_path = './data/lesmis.gml'

graph = nx.read_gml(gml_file_path)

print('Les Miserables graph loaded\n')
