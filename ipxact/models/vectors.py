from dataclasses import dataclass, field

from ipxact.models.vector import Vector

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Vectors:
    """
    Vectored information.
    """

    class Meta:
        name = "vectors"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    vector: list[Vector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
