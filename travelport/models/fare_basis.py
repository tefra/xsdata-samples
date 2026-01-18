from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FareBasis:
    """
    Fare Basis Code.

    Parameters
    ----------
    code
        The fare basis code for this fare
    segment_ref
        The segment to which this FareBasis Code is to connected
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        },
    )
