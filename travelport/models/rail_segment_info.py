from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_rail_segment_info import TypeRailSegmentInfo

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailSegmentInfo:
    """
    A textual remark container to hold any printable text. (max 512 chars)
    Holds the ExtraSegmentInfo and VendorMessages from RCH response.

    Parameters
    ----------
    value
    category
        Supplier specific category.
    type_value
        Either Extra for ExtraSegmentInfo or Vendor for VendorMessages.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        },
    )
    type_value: TypeRailSegmentInfo = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
