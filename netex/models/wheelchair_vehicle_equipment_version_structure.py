from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .actual_vehicle_equipment_version_structure import (
    ActualVehicleEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WheelchairVehicleEquipmentVersionStructure(
    ActualVehicleEquipmentVersionStructure
):
    class Meta:
        name = "WheelchairVehicleEquipment_VersionStructure"

    has_wheelchair_spaces: bool | None = field(
        default=None,
        metadata={
            "name": "HasWheelchairSpaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_wheelchair_areas: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfWheelchairAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width_of_access_area: Decimal | None = field(
        default=None,
        metadata={
            "name": "WidthOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length_of_access_area: Decimal | None = field(
        default=None,
        metadata={
            "name": "LengthOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_of_access_area: Decimal | None = field(
        default=None,
        metadata={
            "name": "HeightOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_turning_circle: Decimal | None = field(
        default=None,
        metadata={
            "name": "WheelchairTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    companion_seat: bool | None = field(
        default=None,
        metadata={
            "name": "CompanionSeat",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
