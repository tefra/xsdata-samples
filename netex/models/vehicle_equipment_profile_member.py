from __future__ import annotations

from dataclasses import dataclass

from .vehicle_equipment_profile_member_version_structure import (
    VehicleEquipmentProfileMemberVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEquipmentProfileMember(
    VehicleEquipmentProfileMemberVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
