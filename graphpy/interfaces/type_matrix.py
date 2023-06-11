from typing import Tuple

from . import AbstractAdjacent, AbstractIncident


class AdjacentMatrix(AbstractAdjacent):
    __slots__ = ()

    def __init__(self, quantity_vertex: int, /, *, weighted: bool):
        super().__init__(quantity_vertex, weighted)

    def __setitem__(
        self, vertex: int, arrival_vertex: int | Tuple[int, int | float]
    ):
        if not isinstance(arrival_vertex, tuple) and super().weighted:
            raise TypeError(
                'Cannot pass arrival vertex without weight when '
                'weighted is true'
            )

        weight: int | float = 0

        if isinstance(arrival_vertex, tuple):
            arrival_vertex, weight = arrival_vertex

        if super().weighted:
            super().data_adj[vertex][arrival_vertex] = weight

        else:
            super().data_adj[vertex][arrival_vertex] = 1

    def __repr__(self):
        return f'AdjacentMatrix(\
            shape={super().shape}, weighted={super().weighted})'


class IncidentMatrix(AbstractIncident):
    __slots__ = ()

    def __init__(self, shape: Tuple[int, int], /):
        super().__init__(shape)
