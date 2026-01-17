from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.slice_type import SliceType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class SlicesType:
    """
    Each slice specifies the HDL path for part of the parent IP-XACT
    object.

    The slices must be concatenated to calculate the entire path. If there
    is only one slice, it is assumed to be the path for the entire IP-XACT
    object.

    :ivar slice: The HDL path for a slice of the IP-XACT object.
    :ivar id:
    """

    class Meta:
        name = "slicesType"

    slice: list[SliceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
