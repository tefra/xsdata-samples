from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.left import Left
from ipxact.models.right import Right

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Arrays:
    """
    :ivar array: Specific left and right array bounds.
    """

    class Meta:
        name = "arrays"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    array: list[Arrays.Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Array:
        left: None | Left = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        right: None | Right = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        array_id: None | str = field(
            default=None,
            metadata={
                "name": "arrayId",
                "type": "Attribute",
            },
        )
        id: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
