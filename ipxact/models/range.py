from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.left import Left
from ipxact.models.right import Right

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Range:
    """
    Left and right bound of a reference into a vector.
    """

    class Meta:
        name = "range"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

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
