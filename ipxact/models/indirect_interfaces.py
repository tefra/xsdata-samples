from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.indirect_interface import IndirectInterface

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class IndirectInterfaces:
    """
    A list of bus interfaces supported by this component.
    """

    class Meta:
        name = "indirectInterfaces"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    indirect_interface: list[IndirectInterface] = field(
        default_factory=list,
        metadata={
            "name": "indirectInterface",
            "type": "Element",
            "min_occurs": 1,
        },
    )
