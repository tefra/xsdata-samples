from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.parking_equipment_or_service_facility import (
    ParkingEquipmentOrServiceFacility,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingSpaceBasicsEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility:
    class Meta:
        name = "_ParkingSpaceBasicsEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacility"

    parking_equipment_or_service_facility: ParkingEquipmentOrServiceFacility | None = field(
        default=None,
        metadata={
            "name": "parkingEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    equipment_or_service_facility_index: int | None = field(
        default=None,
        metadata={
            "name": "equipmentOrServiceFacilityIndex",
            "type": "Attribute",
            "required": True,
        },
    )
