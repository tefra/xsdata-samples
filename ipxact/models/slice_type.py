from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.path_segment_type import PathSegmentType
from ipxact.models.range import Range

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class SliceType:
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
        name = "sliceType"

    path_segments: SliceType.PathSegments = field(
        metadata={
            "name": "pathSegments",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    range: None | Range = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass(kw_only=True)
    class PathSegments:
        path_segment: list[PathSegmentType] = field(
            default_factory=list,
            metadata={
                "name": "pathSegment",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )
