from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.left import Left
from ipxact.models.right import Right

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Vector:
    """
    Left and right ranges of the vector.
    """

    class Meta:
        name = "vector"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    left: Optional[Left] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    right: Optional[Right] = field(
        default=None,
        metadata={
            "type": "Element",
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
