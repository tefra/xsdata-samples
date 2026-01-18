from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.electric_charging import ElectricCharging
from datexii.models.eu.datexii.v2.equipment_type_enum import EquipmentTypeEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.parking_equipment_or_service_facility import (
    ParkingEquipmentOrServiceFacility,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Equipment(ParkingEquipmentOrServiceFacility):
    """
    One type of equipment, that is available on the parking site.

    :ivar equipment_type: One type of equipment, that is available on
        the parking site.
    :ivar electric_charging:
    :ivar equipment_extension:
    """

    equipment_type: EquipmentTypeEnum | None = field(
        default=None,
        metadata={
            "name": "equipmentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    electric_charging: ElectricCharging | None = field(
        default=None,
        metadata={
            "name": "electricCharging",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    equipment_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "equipmentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
