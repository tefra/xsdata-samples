from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class MemoryRemapRef:
    class Meta:
        name = "memoryRemapRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    memory_remap_ref: str = field(
        metadata={
            "name": "memoryRemapRef",
            "type": "Attribute",
            "required": True,
        }
    )
