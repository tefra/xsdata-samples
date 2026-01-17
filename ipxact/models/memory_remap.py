from dataclasses import dataclass

from ipxact.models.memory_remap_type import MemoryRemapType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class MemoryRemap(MemoryRemapType):
    """
    Additional memory map elements that are dependent on the component
    state.
    """

    class Meta:
        name = "memoryRemap"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
