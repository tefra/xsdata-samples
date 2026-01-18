from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.indices import Indices
from ipxact.models.range import Range

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class PartSelect:
    """
    Bit range definition.
    """

    class Meta:
        name = "partSelect"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    range: list[Range] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        },
    )
    indices: None | Indices = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
