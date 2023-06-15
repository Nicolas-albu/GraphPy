"""
This module provides the Graph class for creating and manipulating graphs.
"""

from collections import deque
from typing import Optional

from .error import WeightNotEnabledError
from .graph_list import GraphList


class Graph:
    """
    Represents a graph.

        Graph theory is a branch of mathematics that deals with the study of
    graphs, which are mathematical structures used to represent relationships
    between objects. In graph theory, various representations are employed to
    describe and analyze graphs. Four commonly used representations are
    adjacency matrices, incidence matrices, adjacency lists, and incidence
    lists. Each representation has its own advantages and serves specific
    purposes in graph theory.
    """

    __slots__ = (
        '__directed',
        '__weighted',
        '__data',
    )

    def __init__(
        self,
        *,
        directed: bool = True,
        weighted: bool = False,
    ):
        """Initializes a new instance of the Graph class.

        Args:
            directed (bool): Indicates whether the graph is directed (True)
                or undirected (False).
            weighted (bool): Indicates whether the graph has weighted edges
                (True) or unweighted edges (False).
        """
        self.__directed = directed
        self.__weighted = weighted
        self.__data = GraphList(weighted=self.__weighted)

    @property
    def quantity_rows(self) -> bool:
        """
        Returns the number of rows in the graph.

        Returns:
            int: The number of rows in the graph.
        """
        return self.__data.quantity_rows

    @property
    def is_directed(self) -> bool:
        """
        Checks if the graph is directed.

        Returns:
            bool: True if the graph is directed, False otherwise.
        """
        return self.__directed

    @property
    def is_weighted(self) -> bool:
        """
        Checks if the graph has weighted edges.

        Returns:
            bool: True if the graph has weighted edges, False otherwise.
        """
        return self.__weighted

    @property
    def vertices(self):
        """
        Returns the vertices of the graph.

        Returns:
            list: A list of vertices in the graph.
        """
        return self.__data.vertices

    def put_edge(
        self,
        start_vertex: int | str,
        arrival_vertex: int | str,
        /,
        *,
        weight: Optional[float] = None,
    ) -> None:
        """
        Adds an edge to the graph between the start_vertex and arrival_vertex.

        Args:
            start_vertex (int or str): The starting vertex of the edge.
            arrival_vertex (int or str): The arrival vertex of the edge.
            weight (float, optional): The weight of the edge. Default is None.
        Raises:
            IndexError: If start_vertex or arrival_vertex is an integer less
                than 0.
            WeightNotEnabledError: If weight is provided and the graph is
                unweighted, or if weight is not provided and the graph is
                weighted.
        """
        if isinstance(start_vertex, int) and start_vertex < 0:
            raise IndexError(
                f'arrival vertex {start_vertex!r} cannot be less than zero.'
            )

        if isinstance(arrival_vertex, int) and arrival_vertex < 0:
            raise IndexError(
                f'arrival vertex {arrival_vertex!r} cannot be less than zero.'
            )

        if weight and not self.is_weighted or not weight and self.is_weighted:
            raise WeightNotEnabledError(
                'Cannot insert or not insert value for edge weight in'
                'unweighted graph'
            )

        self.__data.put(start_vertex, arrival_vertex, weight)

        if not self.is_directed:
            self.__data.put(arrival_vertex, start_vertex, weight)

    def __getitem__(self, id_vertex: int) -> deque:
        """
        Returns the adjacent vertices of a given vertex.

        Args:
            id_vertex (int): The identifier of the vertex.
        Returns:
            deque: The deque containing the adjacent vertices.
        """
        return self.__data[id_vertex]

    def __str__(self):
        """
        Returns a string representation of the graph.

        Returns:
            str: A string representation of the graph.
        """
        return str(self.__data)

    def __repr__(self):
        """
        Returns a string representation of the graph.

        Returns:
            str: A string representation of the graph.
        """
        return (
            f'graphpy.Graph(directed={self.__directed}, '
            f'weighted={self.is_weighted})'
        )
