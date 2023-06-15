from collections import deque

import pytest

from graphpy.graph_list import GraphList, Vertex


@pytest.fixture
def empty_graph():
    return GraphList()


@pytest.fixture
def weighted_graph():
    return GraphList(weighted=True)


def test_graph_creation(empty_graph):
    assert empty_graph.quantity_rows == 0
    assert empty_graph.vertices == deque()
    assert not empty_graph.is_weighted


def test_weighted_graph_creation(weighted_graph):
    assert weighted_graph.is_weighted


def test_graph_put_edge(empty_graph):
    empty_graph.put('A', 'B')
    assert empty_graph.quantity_rows == 2
    assert empty_graph.vertices == deque(
        [
            Vertex(id=1, name='A', adj=deque([2])),
            Vertex(id=2, name='B', adj=deque([])),
        ]
    )
    assert empty_graph[1] == deque([2])
    assert empty_graph[2] == deque([])


def test_graph_put_edge_with_weight(weighted_graph):
    weighted_graph.put('A', 'B', 3.5)
    assert weighted_graph.quantity_rows == 2
    assert weighted_graph.vertices == deque(
        [
            Vertex(id=1, name='A', adj=deque([(2, 3.5)])),
            Vertex(id=2, name='B', adj=deque([])),
        ]
    )
    assert weighted_graph[1] == deque([(2, 3.5)])
    assert weighted_graph[2] == deque([])


def test_graph_str_representation(empty_graph):
    empty_graph.put('A', 'B')
    expected_str = "1: A -> [2]\n2: B -> []\n"
    assert str(empty_graph) == expected_str


def test_graph_repr_representation(empty_graph):
    assert repr(empty_graph) == "GraphList(weighted=False)"
