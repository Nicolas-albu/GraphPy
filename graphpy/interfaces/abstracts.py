from abc import ABC, abstractmethod
from typing import Tuple

import numpy as np


class AbstractAdjacent(ABC):
    """
    Abstract base class for representing an adjacency structure.

    Args:
        quantity_vertex (int): The number of vertices in the adjacency
            structure.
        weighted (bool): Indicates whether the adjacency structure is weighted.

    Attributes:
        shape: The shape of the adjacency structure.
        weighted: Indicates whether the adjacency structure is weighted.
        data_adj: The adjacency data structure.

    Methods:
        __setitem__: Sets the arrival vertex for a given vertex in the
            adjacency structure.
        __repr__: Returns a string representation of the adjacency structure.
        __getitem__: Returns the arrival vertex of a given vertex in the
            adjacency structure.
        __str__: Returns a string representation of the adjacency structure.
    """

    def __init__(self, quantity_vertex: int, weighted: bool, /):
        self.__shape = (quantity_vertex,) * 2
        self.__data_adj = np.zeros(self.__shape)
        self.__weighted = weighted

    @abstractmethod
    def __setitem__(
        self, vertex: int, arrival_vertex: int | Tuple[int, int | float]
    ):
        raise NotImplementedError

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError

    @property
    def shape(self):
        return self.__shape

    @property
    def weighted(self):
        return self.__weighted

    @property
    def data_adj(self):
        return self.__data_adj

    def __getitem__(self, vertex: int) -> int | float:
        return self.data_adj[vertex]

    def __str__(self):
        return str(self.data_adj)


class AbstractIncident(ABC):
    def __init__(self, shape: Tuple[int, int], /):
        self.__shape = shape
        self.__inc = np.zeros(shape)

    @abstractmethod
    def __setitem__(
        self, vertex: int, arrival_vertex: int | Tuple[int, int | float]
    ):
        raise NotImplementedError

    @abstractmethod
    def __getitem__(self, vertex: int):
        raise NotImplementedError

    @property
    def shape(self):
        return self.__shape

    @property
    def inc(self):
        return self.__inc

    @inc.setter
    def inc(self, value):
        self.__inc = value

    def set_incident(
        self, vertex: int, arrival_vertex: Tuple[int, int | float]
    ) -> None:
        # arrival_vertex, weight = arrival_vertex
        # self.__inc[vertex] = weight
        # self.__inc[arrival_vertex] = weight
        ...
