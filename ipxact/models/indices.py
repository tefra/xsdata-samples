from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.indices_type import IndicesType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Indices(IndicesType):
    class Meta:
        name = "indices"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
