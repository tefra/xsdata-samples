from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.row import Row

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Rows:
    """A wrapper for all the information regarding each of the rows.

    Providers: ACH, 1G, 1V, 1P

    Parameters
    ----------
    row
        Provider: 1G,1V,1P,ACH,MCH.
    segment_ref
        Specifies the AirSegment the seat map is for. Providers: ACH, 1G,
        1V, 1P
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    row: list[Row] = field(
        default_factory=list,
        metadata={
            "name": "Row",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
