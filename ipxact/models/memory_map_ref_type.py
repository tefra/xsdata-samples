from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class MemoryMapRefType:
    """Base type for an element which references an memory map.

    Reference is kept in an attribute rather than the text value, so
    that the type may be extended with child elements if necessary.

    :ivar mode_ref:
    :ivar memory_map_ref: A reference to a unique memory map.
    """

    class Meta:
        name = "memoryMapRefType"

    mode_ref: list["MemoryMapRefType.ModeRef"] = field(
        default_factory=list,
        metadata={
            "name": "modeRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    memory_map_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "memoryMapRef",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class ModeRef:
        """
        A reference to a mode.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
