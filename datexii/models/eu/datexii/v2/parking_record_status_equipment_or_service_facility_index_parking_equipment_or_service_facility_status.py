from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.parking_equipment_or_service_facility_status import (
    ParkingEquipmentOrServiceFacilityStatus,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingRecordStatusEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacilityStatus:
    class Meta:
        name = "_ParkingRecordStatusEquipmentOrServiceFacilityIndexParkingEquipmentOrServiceFacilityStatus"

    parking_equipment_or_service_facility_status: ParkingEquipmentOrServiceFacilityStatus | None = field(
        default=None,
        metadata={
            "name": "parkingEquipmentOrServiceFacilityStatus",
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
