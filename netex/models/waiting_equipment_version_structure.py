from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .site_equipment_version_structure import SiteEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WaitingEquipmentVersionStructure(SiteEquipmentVersionStructure):
    class Meta:
        name = "WaitingEquipment_VersionStructure"

    seats: int | None = field(
        default=None,
        metadata={
            "name": "Seats",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Decimal | None = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length: Decimal | None = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_free: bool | None = field(
        default=None,
        metadata={
            "name": "StepFree",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_area_width: Decimal | None = field(
        default=None,
        metadata={
            "name": "WheelchairAreaWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_area_length: Decimal | None = field(
        default=None,
        metadata={
            "name": "WheelchairAreaLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    smoking_allowed: bool | None = field(
        default=None,
        metadata={
            "name": "SmokingAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    heated: bool | None = field(
        default=None,
        metadata={
            "name": "Heated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    air_conditioned: bool | None = field(
        default=None,
        metadata={
            "name": "AirConditioned",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
