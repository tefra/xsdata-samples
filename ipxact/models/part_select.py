from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.indices import Indices
from ipxact.models.range import Range

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
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
    indices: Indices | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
