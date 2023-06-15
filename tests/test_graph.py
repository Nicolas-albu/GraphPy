from collections import deque

import pytest

from graphpy import Graph
from graphpy.error import WeightNotEnabledError
from graphpy.graph_list import Vertex


@pytest.fixture
def graph():
    return Graph()


@pytest.fixture
def graph_weighted():
    return Graph(weighted=True)


def test_graph_creation(graph):
    assert graph.is_directed
    assert not graph.is_weighted
    assert graph.quantity_rows == 0
    assert graph.vertices == deque()

    graph = Graph(directed=False, weighted=True)
    assert not graph.is_directed
    assert graph.is_weighted


def test_graph_put_edge(graph):
    graph.put_edge(1, 2)

    deque_vertex_one = deque()
    deque_vertex_one.append(2)
    vertex_one = Vertex(1, 1, deque_vertex_one)
    vertex_two = Vertex(2, 2, deque())

    vertices = deque()
    vertices.append(vertex_one)
    vertices.append(vertex_two)

    assert graph.quantity_rows == 2
    assert graph.vertices == vertices
    assert graph[1] == deque([2])
    assert graph[2] == deque([])


def test_graph_put_edge_with_weight(graph_weighted):
    graph_weighted.put_edge('A', 'B', weight=2.5)

    deque_vertex_A = deque()
    deque_vertex_A.append((2, 2.5))
    vertex_A = Vertex(1, 'A', deque_vertex_A)
    vertex_B = Vertex(2, 'B', deque())

    vertices = deque()
    vertices.append(vertex_A)
    vertices.append(vertex_B)

    assert graph_weighted.quantity_rows == 2
    assert graph_weighted.vertices == vertices
    assert graph_weighted[1] == deque([(2, 2.5)])
    assert graph_weighted[2] == deque([])


def test_graph_put_edge_invalid_vertex(graph):
    with pytest.raises(IndexError):
        graph.put_edge(-1, 2)

    with pytest.raises(IndexError):
        graph.put_edge('A', -2)


def test_graph_put_edge_invalid_weight():
    graph = Graph(weighted=False)
    with pytest.raises(WeightNotEnabledError):
        graph.put_edge(1, 2, weight=3.2)

    with pytest.raises(WeightNotEnabledError):
        graph.put_edge('A', 'B', weight=2.5)


def test_graph_str_representation(graph):
    graph.put_edge(1, 2)
    graph.put_edge(2, 3)
    graph.put_edge('A', 'B')

    expected_str = (
        '1: 1 -> [2]\n2: 2 -> [3]\n3: 3 -> []\n4: A -> [5]\n5: B -> []\n'
    )
    assert str(graph) == expected_str


def test_graph_repr_representation():
    graph = Graph()
    assert repr(graph) == "graphpy.Graph(directed=True, weighted=False)"

    graph = Graph(directed=False, weighted=True)
    assert repr(graph) == "graphpy.Graph(directed=False, weighted=True)"
