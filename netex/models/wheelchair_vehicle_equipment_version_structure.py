from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .actual_vehicle_equipment_version_structure import (
    ActualVehicleEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WheelchairVehicleEquipmentVersionStructure(
    ActualVehicleEquipmentVersionStructure
):
    class Meta:
        name = "WheelchairVehicleEquipment_VersionStructure"

    has_wheelchair_spaces: None | bool = field(
        default=None,
        metadata={
            "name": "HasWheelchairSpaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_wheelchair_areas: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfWheelchairAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width_of_access_area: None | Decimal = field(
        default=None,
        metadata={
            "name": "WidthOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length_of_access_area: None | Decimal = field(
        default=None,
        metadata={
            "name": "LengthOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height_of_access_area: None | Decimal = field(
        default=None,
        metadata={
            "name": "HeightOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_turning_circle: None | Decimal = field(
        default=None,
        metadata={
            "name": "WheelchairTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    companion_seat: None | bool = field(
        default=None,
        metadata={
            "name": "CompanionSeat",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
