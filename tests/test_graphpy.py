import pytest

from graphpy import Graph


@pytest.fixture
def graph():
    shape = (6, 6)
    sparse = False
    directed = True
    weighted = False
    return Graph(shape, sparse=sparse, directed=directed, weighted=weighted)


@pytest.fixture
def graph_with_weight():
    shape = (10, 10)
    sparse = False
    directed = True
    weighted = True
    return Graph(shape, sparse=sparse, directed=directed, weighted=weighted)


def test_graph_creation(graph):
    assert graph.shape == (6, 6)
    assert graph.is_sparse is False
    assert graph.is_directed is True
    assert graph.is_weighted is False


def test_graph_set_and_get_item(graph):
    graph[1] = 2
    assert graph[1][2] == 1


def test_graph_set_and_get_item_with_weight(graph_with_weight):
    graph_with_weight[1] = (2, 0.5)
    assert graph_with_weight[1][2] == 0.5
