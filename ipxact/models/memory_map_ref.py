from __future__ import annotations

from dataclasses import dataclass

from ipxact.models.memory_map_ref_type import MemoryMapRefType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class MemoryMapRef(MemoryMapRefType):
    """
    References the memory map.

    The name of the memory map is kept in its memoryMapRef attribute.
    """

    class Meta:
        name = "memoryMapRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
