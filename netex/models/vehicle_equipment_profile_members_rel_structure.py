from dataclasses import dataclass, field
from typing import List

from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .vehicle_equipment_profile_member import VehicleEquipmentProfileMember

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEquipmentProfileMembersRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "vehicleEquipmentProfileMembers_RelStructure"

    vehicle_equipment_profile_member: List[VehicleEquipmentProfileMember] = (
        field(
            default_factory=list,
            metadata={
                "name": "VehicleEquipmentProfileMember",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
