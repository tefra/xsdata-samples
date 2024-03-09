from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_associated_remark_3 import TypeAssociatedRemark3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class TypeAssociatedRemarkWithSegmentRef3(TypeAssociatedRemark3):
    """
    A textual remark container to hold Associated itinerary remarks with segment
    association.

    Parameters
    ----------
    segment_ref
        Reference to an Air/Passive Segment
    """

    class Meta:
        name = "typeAssociatedRemarkWithSegmentRef"

    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        },
    )
