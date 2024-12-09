from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.left import Left
from ipxact.models.right import Right

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ConfigurableArrays:
    """
    :ivar array: Specific left and right array bounds.
    """

    class Meta:
        name = "configurableArrays"

    array: list["ConfigurableArrays.Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Array:
        left: Optional[Left] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
            },
        )
        right: Optional[Right] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
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
