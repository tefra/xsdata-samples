from dataclasses import dataclass, field
from typing import Optional
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.boarding_position_ref import BoardingPositionRef
from netex.models.stop_place_entrance_ref import StopPlaceEntranceRef
from netex.models.vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePositionAlignmentVersionStructure(VersionedChildStructure):
    class Meta:
        name = "VehiclePositionAlignment_VersionStructure"

    vehicle_stopping_position_ref: Optional[VehicleStoppingPositionRef] = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_position_ref: Optional[BoardingPositionRef] = field(
        default=None,
        metadata={
            "name": "BoardingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_entrance_ref: Optional[StopPlaceEntranceRef] = field(
        default=None,
        metadata={
            "name": "StopPlaceEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
