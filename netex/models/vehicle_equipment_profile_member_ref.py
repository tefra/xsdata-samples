from __future__ import annotations

from dataclasses import dataclass

from .vehicle_equipment_profile_member_ref_structure import (
    VehicleEquipmentProfileMemberRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEquipmentProfileMemberRef(
    VehicleEquipmentProfileMemberRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
