from __future__ import annotations

from dataclasses import dataclass, field

from .stair_equipment_version_structure import StairEquipmentVersionStructure
from .stair_flights_rel_structure import StairFlightsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StaircaseEquipmentVersionStructure(StairEquipmentVersionStructure):
    class Meta:
        name = "StaircaseEquipment_VersionStructure"

    continuous_handrail: None | bool = field(
        default=None,
        metadata={
            "name": "ContinuousHandrail",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    without_riser: None | bool = field(
        default=None,
        metadata={
            "name": "WithoutRiser",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spiral_stair: None | bool = field(
        default=None,
        metadata={
            "name": "SpiralStair",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_flights: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfFlights",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flights: None | StairFlightsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
