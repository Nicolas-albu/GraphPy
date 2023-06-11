from typing import Tuple

from . import AbstractAdjacent, AbstractIncident


class Edge:
    def __init__(self):
        ...


class Vertex:
    def __init__(self):
        ...


class AdjacentList(AbstractAdjacent):
    __slots__ = ()

    def __init__(self, quantity_vertex: int, /, *, weighted: bool):
        super().__init__(quantity_vertex, weighted)

    def __setitem__(
        self, vertex: int, arrival_vertex: int | Tuple[int, int | float]
    ):
        ...

    def __repr__(self):
        return (
            f'AdjacentList(shape={super().shape}, weighted={super().weighted})'
        )


class IncidentList(AbstractIncident):
    __slots__ = ()

    def __init__(self, shape: Tuple[int, int], /):
        super().__init__(shape)
