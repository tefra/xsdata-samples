from dataclasses import dataclass, field

from ipxact.models.index import Index

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class IndicesType:
    class Meta:
        name = "indicesType"

    index: list[Index] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
        },
    )
