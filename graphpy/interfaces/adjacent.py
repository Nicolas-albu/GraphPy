from abc import ABC, abstractmethod
from typing import Tuple

import numpy as np


class AbstractAdjacent(ABC):
    def __init__(self, shape: int | Tuple[int, int], weighted: bool, /):
        self.__shape = shape
        self.__adj = np.zeros(shape)
        self.__weighted = weighted

    @abstractmethod
    def __setitem__(
        self, vertex: int, arrival_vertex: int | Tuple[int, int | float]
    ):
        raise NotImplementedError

    @property
    def shape(self):
        return self.__shape

    @property
    def weighted(self):
        return self.__weighted

    @property
    def adj(self):
        return self.__adj

    @adj.setter
    def adj(self, value):
        self.__adj = value

    def __getitem__(self, vertex: int) -> int | float:
        return self.__adj[vertex]

    def __str__(self):
        return str(self.__adj)


class AdjacentList(AbstractAdjacent):
    def __init__(self, shape: int | Tuple[int, int], /, *, weighted: bool):
        super().__init__(shape, weighted)

    def __setitem__(
        self, vertex: int, arrival_vertex: int | Tuple[int, int | float]
    ):
        ...

    def __repr__(self):
        return f'AdjacentList({super().shape=}, {super().weighted=})'


class AdjacentMatrix(AbstractAdjacent):
    def __init__(self, shape: int | Tuple[int, int], /, *, weighted: bool):
        super().__init__(shape, weighted)

    def __setitem__(
        self, vertex: int, arrival_vertex: int | Tuple[int, int | float]
    ):
        if isinstance(arrival_vertex, Tuple) and super().weighted:
            arrival_vertex, weight = arrival_vertex
            vertex, arrival_vertex = vertex - 1, arrival_vertex - 1

            super().adj[vertex][arrival_vertex] = weight
        else:
            if (vertex, arrival_vertex) >= (0, 0):
                vertex, arrival_vertex = vertex - 1, arrival_vertex - 1

            super().adj[vertex][arrival_vertex] = 1

    def __repr__(self):
        return f'AdjacentMatrix({super().shape=}, {super().weighted=})'
