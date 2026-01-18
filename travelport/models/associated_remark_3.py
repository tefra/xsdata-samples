from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_associated_remark_1 import TypeAssociatedRemark1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class AssociatedRemark3(TypeAssociatedRemark1):
    class Meta:
        name = "AssociatedRemark"
        namespace = "http://www.travelport.com/schema/hotel_v52_0"
