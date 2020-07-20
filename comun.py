import networkx as nx
from pycliques.cliques import clique_graph as k
from pycliques.dominated import completely_pared_graph as p
from pycliques.dominated import complete_s_collapse, complete_s_collapse_edges
from pycliques.surfaces import open_neighborhood


def pk(graph):
    the_graph = k(graph, 1300)
    the_graph = nx.convert_node_labels_to_integers(the_graph)
    return p(the_graph)


# gap lists are indexed from 1
def gap_adyacency_list(graph):
    graph = nx.convert_node_labels_to_integers(graph)
    pre_list = [list(graph[i]) for i in graph.nodes()]
    return [[i+1 for i in neigh] for neigh in pre_list]


def simplify_ht(g):
    vg = complete_s_collapse(g)
    evg = complete_s_collapse_edges(vg)
    return evg


def is_contractible(g):
    return simplify_ht(g).order() == 1


def dong_matching(graph):
    matched = []
    vertices = list(graph.nodes())
    all_completes = list(nx.enumerate_all_cliques(graph))
    all_completes.append([])
    all_completes = set([frozenset(c) for c in all_completes])
    for vertex in vertices:
        neigh = open_neighborhood(graph, vertex)
        completes = list(nx.enumerate_all_cliques(neigh))
        completes.append([])
        for complete in completes:
            complete = frozenset(complete)
            if (complete not in matched) \
               and (not complete | {vertex} in matched):
                matched.append(complete)
                matched.append(complete | {vertex})
    return all_completes - set(matched)
