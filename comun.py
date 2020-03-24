import networkx as nx
from pycliques.cliques import clique_graph as k
from pycliques.dominated import completely_pared_graph as p
from pycliques.dominated import complete_s_collapse, complete_s_collapse_edges


def pk(graph):
    the_graph = k(graph, 1300)
    the_graph = nx.convert_node_labels_to_integers(the_graph)
    return p(the_graph)


# gap lists are indexed from 1
def gap_adyacency_list(graph):
    graph = nx.convert_node_labels_to_integers(graph)
    pre_list = [list(graph[i]) for i in graph.nodes()]
    return [[i+1 for i in neigh] for neigh in pre_list]


def is_contractible(g):
    vg = complete_s_collapse(g)
    evg = complete_s_collapse_edges(vg)
    return gap_adyacency_list(evg) == [[]]
