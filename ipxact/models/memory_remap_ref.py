from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class MemoryRemapRef:
    class Meta:
        name = "memoryRemapRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    memory_remap_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "memoryRemapRef",
            "type": "Attribute",
            "required": True,
        },
    )
