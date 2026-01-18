from __future__ import annotations

from dataclasses import dataclass, field

from .multilingual_string import MultilingualString
from .relation_to_vehicle_enumeration import RelationToVehicleEnumeration
from .stop_place_component_version_structure import (
    StopPlaceComponentVersionStructure,
)
from .vehicle_position_alignments_rel_structure import (
    VehiclePositionAlignmentsRelStructure,
)
from .vehicle_stopping_place_ref import VehicleStoppingPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPositionVersionStructure(
    StopPlaceComponentVersionStructure
):
    class Meta:
        name = "VehicleStoppingPosition_VersionStructure"

    vehicle_stopping_place_ref: VehicleStoppingPlaceRef | None = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    relation_to_vehicle: RelationToVehicleEnumeration | None = field(
        default=None,
        metadata={
            "name": "RelationToVehicle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bearing: int | None = field(
        default=None,
        metadata={
            "name": "Bearing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_position_alignments: (
        VehiclePositionAlignmentsRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "vehiclePositionAlignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
