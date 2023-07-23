from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_associated_remark_with_segment_ref_1 import TypeAssociatedRemarkWithSegmentRef1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AssociatedRemark1(TypeAssociatedRemarkWithSegmentRef1):
    class Meta:
        name = "AssociatedRemark"
        namespace = "http://www.travelport.com/schema/air_v52_0"
