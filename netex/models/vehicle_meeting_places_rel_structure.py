from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_meeting_place_2 import VehicleMeetingPlace2
from .vehicle_pooling_meeting_place import VehiclePoolingMeetingPlace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleMeetingPlaces_RelStructure"

    vehicle_meeting_place: List[
        Union[VehiclePoolingMeetingPlace, VehicleMeetingPlace2]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingMeetingPlace",
                    "type": VehiclePoolingMeetingPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPlace_",
                    "type": VehicleMeetingPlace2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
