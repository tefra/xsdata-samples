from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_associated_remark_1 import TypeAssociatedRemark1

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class AssociatedRemark2(TypeAssociatedRemark1):
    class Meta:
        name = "AssociatedRemark"
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"
