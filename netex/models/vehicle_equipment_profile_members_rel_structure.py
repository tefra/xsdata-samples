from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .vehicle_equipment_profile_member import VehicleEquipmentProfileMember

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEquipmentProfileMembersRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "vehicleEquipmentProfileMembers_RelStructure"

    vehicle_equipment_profile_member: Sequence[
        VehicleEquipmentProfileMember
    ] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEquipmentProfileMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
