"""
This module provides the Graph class for creating and manipulating graphs.
"""

from typing import Tuple

from .error import GraphIncompatibleError
from .interfaces import (
    AbstractAdjacent,
    AbstractIncident,
    AdjacentList,
    AdjacentMatrix,
)


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

    Adjacency Matrices:
        An adjacency matrix is a square matrix used to represent the
        connections between vertices in a graph. The rows and columns of the
        matrix correspond to the vertices of the graph, and each entry
        represents the presence or absence of an edge between two vertices. If
        there is an edge between vertices i and j, the corresponding entry in
        the matrix is set to 1; otherwise, it is set to 0. Adjacency matrices
        are particularly useful for dense graphs, where the number of edges is
        close to the maximum possible number of edges.

    Incidence Matrices:
        An incidence matrix is a rectangular matrix used to represent the
    relationships between vertices and edges in a graph. The rows of the
    matrix correspond to the vertices, and the columns correspond to the edges.
    Each entry indicates the incidence of a vertex in an edge. Typically, the
    entry is set to 1 if the vertex is incident to the edge, -1 if the vertex
    is incident to the edge but in the opposite direction, and 0 if the vertex
    is not incident to the edge. Incidence matrices are commonly used for
    directed graphs or graphs with multiple edges between vertices.

    Adjacency Lists:
        An adjacency list is a data structure that represents a graph as an
    array of linked lists. Each element in the array corresponds to a vertex
    in the graph, and the linked list associated with each vertex contains the
    vertices that are adjacent to it. Adjacency lists are memory-efficient for
    representing sparse graphs, where the number of edges is significantly
    smaller than the maximum possible number of edges. They also facilitate
    efficient traversal of a graph, as it is easy to obtain a list of adjacent
    vertices for a given vertex.

    Incidence Lists:
        An incidence list is a data structure that represents a graph as an
    array of linked lists. Similar to adjacency lists, each element in the
    array corresponds to a vertex in the graph. However, the linked list
    associated with each vertex contains the edges incident to that vertex
    rather than the adjacent vertices. Incidence lists are commonly used when
    the focus is on the relationships between vertices and edges, rather than
    adjacency between vertices.
    """

    __slots__ = (
        '__quantity_vertex',
        '__quantity_edges',
        '__shape',
        '__sparse',
        '__directed',
        '__weighted',
        '__data',
    )

    def __init__(
        self,
        shape: Tuple[int, int],
        *,
        sparse: bool,
        directed: bool,
        weighted: bool,
    ):
        """Initializes a new instance of the Graph class.

        Args:
            shape (Tuple[int, int]): The shape of the graph, represented by an
                ordered pair of integers, where the first value is the number
                of vertices and the second value is the number of edges.
            sparse (bool): Indicates whether the graph is sparse (True)
                or dense (False).
            directed (bool): Indicates whether the graph is directed (True)
                or undirected (False).
            weighted (bool): Indicates whether the graph has weighted edges
                (True) or unweighted edges (False).
        """
        self.__quantity_vertex, self.__quantity_edges = shape
        self.__shape = shape
        self.__sparse = sparse
        self.__directed = directed
        self.__weighted = weighted
        self.__data = self.__factory_data()

    @property
    def shape(self) -> Tuple[int, int]:
        """
        Gets the shape of the graph.

        Returns:
            Tuple[int, int]: The shape of the graph, represented by an ordered
                pair of integers, where the first value
            is the number of vertices and the second value is the number
                of edges.
        """
        return self.__shape

    @property
    def is_sparse(self) -> bool:
        """
        Checks if the graph is sparse.

        Returns:
            bool: True if the graph is sparse, False otherwise.
        """
        return self.__sparse

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

    def __factory_data(self) -> AbstractAdjacent | AbstractIncident:
        """
        Factory method to create the appropriate data structure based on the
            graph properties.

        Returns:
            AbstractAdjacent | AbstractIncident: An instance of a class
                implementing either the AbstractAdjacent or
            AbstractIncident interface, based on the graph properties.
        Raises:
            GraphIncompatibleError: If the graph type is incompatible.
        """
        is_more_vertex: bool = self.__quantity_edges <= self.__quantity_vertex

        if is_more_vertex and self.is_sparse:
            return AdjacentList(
                self.__quantity_vertex, weighted=self.is_weighted
            )

        if is_more_vertex:
            return AdjacentMatrix(
                self.__quantity_vertex, weighted=self.is_weighted
            )

        raise GraphIncompatibleError('Incompatible graph types')

    def __setitem__(
        self, vertex: int, arrival_vertex: int | Tuple[int, int | float]
    ):
        """
        Sets the arrival vertex for a given vertex in the graph.

        Args:
            vertex (int): The vertex to set the arrival vertex for.
            arrival_vertex (int | Tuple[int, int | float]): The arrival vertex
                or an ordered pair of the arrival vertex and its weight
                (if the graph is weighted).
        Raises:
            IndexError: If the vertex or arrival vertex is out of range.
            TypeError: If the arrival vertex is not of the expected
        """
        if 0 > vertex < self.__quantity_vertex:
            raise IndexError(f'vertex {vertex!r} does not exist.')

        if not isinstance(arrival_vertex, int | tuple):
            raise TypeError(
                'expected arrival_vertex int or Tuple[int, int | float].'
            )

        weight: int | float = 0

        if is_tuple := isinstance(arrival_vertex, tuple):
            arrival_vertex, weight = arrival_vertex

        if 0 > arrival_vertex < self.__quantity_edges:
            raise IndexError(
                f'arrival vertex {arrival_vertex!r} does not exist.'
            )

        if is_tuple:
            self.__data[vertex] = arrival_vertex, weight

            if self.is_directed:
                self.__data[arrival_vertex] = vertex, weight

        else:
            self.__data[vertex] = arrival_vertex

            if self.is_directed:
                self.__data[arrival_vertex] = vertex

    def __getitem__(self, vertex: int) -> int | float:
        """
        Returns the arrival vertex of a given vertex in the graph.

        Args:
            vertex (int): The vertex to retrieve the arrival vertex for.
        Returns:
            int | float: The arrival vertex or its weight
                (if the graph is weighted).
        """
        return self.__data[vertex]

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
        return repr(self.__data)
