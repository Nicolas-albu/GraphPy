"""
This module provides the GraphList class for implements a graph using an
adjacency list data structure.
"""

from collections import deque
from dataclasses import dataclass
from typing import Any, Generator, Optional


@dataclass
class Vertex:
    """Vertex class for the graph"""

    id: int
    name: str  # Name of vertex (e.g., "A", "B")
    adj: deque


class GraphList:
    """
    Represents a graph using an adjacency list.

    The adjacency list is implemented using a deque of Vertex objects.
    Each Vertex object contains an identifier, a name, and an adjacency list.
    """

    __slots__ = ('__weighted', '__quantity_rows', '__list', '__generator_id')

    def __init__(self, *, weighted: bool = False):
        """
        Initializes a new instance of the GraphList class.

        Args:
            weighted (bool): Indicates whether the graph has weighted edges
                (True) or unweighted edges (False).
        """
        self.__weighted = weighted
        self.__quantity_rows = 0
        self.__list: deque[Vertex] = deque()
        self.__generator_id = self.__next_id()

    @property
    def quantity_rows(self):
        """
        Returns the number of rows (vertices) in the graph.

        Returns:
            int: The number of rows in the graph.
        """
        return self.__quantity_rows

    @property
    def vertices(self) -> deque[Vertex]:
        """
        Returns the vertices of the graph.

        Returns:
            deque: A deque containing the vertices of the graph.
        """
        return self.__list

    @property
    def is_weighted(self) -> bool:
        """
        Checks if the graph has weighted edges.

        Returns:
            bool: True if the graph has weighted edges, False otherwise.
        """
        return self.__weighted

    def __next_id(self) -> Generator[int, Any, None]:
        """
        Generates the next available vertex identifier.

        Yields:
            int: The next available vertex identifier.
        """
        number = 1
        while True:
            yield number
            number += 1

    def __add_row(self, id_vertex, vertex_name) -> None:
        """
        Adds a new row (vertex) to the graph.

        Args:
            id_vertex (int): The identifier of the new vertex.
            vertex_name (str): The name of the new vertex.
        """
        __new_adj = deque()
        __new_row = Vertex(id_vertex, vertex_name, __new_adj)

        self.__list.append(__new_row)
        self.__quantity_rows += 1

    def put(
        self,
        start_vertex: int | str,
        arrival_vertex: int | str,
        weight: Optional[float] = None,
        /,
    ) -> None:
        """
        Adds an edge to the graph between the start_vertex and arrival_vertex.

        Args:
            start_vertex (str): The name of the starting vertex of the edge.
            arrival_vertex (str): The name of the arrival vertex of the edge.
            weight (float, optional): The weight of the edge. Default is None.
        """
        for vertex in self.__list:
            if vertex.name == start_vertex:
                start_vertex = vertex.id
                break
        else:
            __id_vertex = next(self.__generator_id)
            self.__add_row(__id_vertex, start_vertex)
            start_vertex = __id_vertex

        for vertex in self.__list:
            if vertex.name == arrival_vertex:
                arrival_vertex = vertex.id
                break
        else:
            __id_vertex = next(self.__generator_id)
            self.__add_row(__id_vertex, arrival_vertex)
            arrival_vertex = __id_vertex

        __list_position = start_vertex - 1
        if weight:
            self.__list[__list_position].adj.append((arrival_vertex, weight))
        else:
            self.__list[__list_position].adj.append(arrival_vertex)

    def __getitem__(self, id: int) -> deque:
        """
        Returns the adjacency list of the vertex with the given identifier.

        Args:
            id (int): The identifier of the vertex.
        Returns:
            deque: The adjacency list of the vertex.
        """
        __list_position = id - 1
        return self.__list[__list_position].adj

    def __str__(self):
        """
        Returns a string representation of the graph.

        Returns:
            str: A string representation of the graph.
        """
        msg = ''
        for vertex in self.__list:
            msg += f'{vertex.id}: {vertex.name} -> {list(vertex.adj)}\n'

        return msg

    def __repr__(self):
        """
        Returns a string representation of the graph.

        Returns:
            str: A string representation of the graph.
        """
        return f'GraphList(weighted={self.is_weighted})'
