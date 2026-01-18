from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.memory_map_type import MemoryMapType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class MemoryMaps:
    """
    Lists all the target memory maps defined by the component.

    :ivar memory_map: The set of address blocks a bus target contributes
        to the bus' address space.
    """

    class Meta:
        name = "memoryMaps"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    memory_map: list[MemoryMapType] = field(
        default_factory=list,
        metadata={
            "name": "memoryMap",
            "type": "Element",
            "min_occurs": 1,
        },
    )
