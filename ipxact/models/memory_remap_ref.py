from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class MemoryRemapRef:
    class Meta:
        name = "memoryRemapRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    memory_remap_ref: None | str = field(
        default=None,
        metadata={
            "name": "memoryRemapRef",
            "type": "Attribute",
            "required": True,
        },
    )
