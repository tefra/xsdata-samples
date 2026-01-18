from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.port_path_segment_type import PortPathSegmentType
from ipxact.models.range import Range

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class PortSliceType:
    """
    Contains the HDL path information for a slice of the IP-XACT object.

    :ivar path_segments: An ordered list of pathSegment elements. When
        concatenated with a desired separator the elements in this form
        a HDL path for the parent slice into the referenced view.
    :ivar range: A range to be applied to the concatenation of the above
        path segments
    :ivar id:
    """

    class Meta:
        name = "portSliceType"

    path_segments: PortSliceType.PathSegments | None = field(
        default=None,
        metadata={
            "name": "pathSegments",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    range: Range | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class PathSegments:
        path_segment: list[PortPathSegmentType] = field(
            default_factory=list,
            metadata={
                "name": "pathSegment",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )
