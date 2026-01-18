from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.parking_equipment_or_service_facility import (
    ParkingEquipmentOrServiceFacility,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class ParkingSpaceBasicsEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility:
    class Meta:
        name = "_ParkingSpaceBasicsEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility"

    parking_equipment_or_service_facility: ParkingEquipmentOrServiceFacility = field(
        metadata={
            "name": "parkingEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    equipment_or_service_facility_index: int = field(
        metadata={
            "name": "equipmentOrServiceFacilityIndex",
            "type": "Attribute",
            "required": True,
        }
    )
