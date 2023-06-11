from typing import Tuple, Union, overload

from .error import GraphIncompatibleError
from .interfaces import AdjacentList, AdjacentMatrix


class Graph:
    def __init__(
        self,
        shape: Tuple[int, int],
        *,
        sparse: bool,
        directed: bool,
        weighted: bool,
    ):
        self.__quantity_vertex, self.__quantity_edges = shape
        self.__shape = shape
        self.__sparse = sparse
        self.__directed = directed
        self.__weighted = weighted
        self.__data = self.__factory_data()

    def __factory_data(self):
        if (
            is_more_vertex := self.__quantity_edges <= self.__quantity_vertex
        ) and self.__sparse:
            return AdjacentList(
                self.__quantity_vertex, weighted=self.__weighted
            )

        if is_more_vertex:
            return AdjacentMatrix(self.__shape, weighted=self.__weighted)

        raise GraphIncompatibleError('Incompatible graph types')

    @overload
    def __setitem__(self, vertex: int, arrival_vertex: int):
        ...

    def __setitem__(self, vertex, arrival_vertex):
        if not isinstance(arrival_vertex, Union[int, tuple]):
            raise TypeError

        if not vertex >= self.__quantity_vertex and vertex < 0:
            raise IndexError(f'vertex {vertex!r} does not exist.')

        if isinstance(arrival_vertex, tuple):
            next_vertex, weight = arrival_vertex
            if not next_vertex >= self.__quantity_edges and (
                next_vertex,
                weight,
            ) < (0, 0):
                raise IndexError(
                    f'arrival vertex {arrival_vertex!r} does not exist.'
                )
        else:
            if (
                not arrival_vertex >= self.__quantity_edges
                and arrival_vertex < 0
            ):
                raise IndexError(
                    f'arrival vertex {arrival_vertex!r} does not exist.'
                )

        if self.__directed:
            next_vertex, weight = arrival_vertex
            self.__data[next_vertex] = vertex, weight

        self.__data[vertex] = arrival_vertex

    def __getitem__(self, vertex: int) -> int | float:
        return self.__data[vertex - 1]

    def __str__(self):
        return str(self.__data)

    def __repr__(self):
        return self.__data.__repr__()
