from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_meeting_point import VehicleMeetingPoint
from .vehicle_meeting_point_ref import VehicleMeetingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPointsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleMeetingPoints_RelStructure"

    vehicle_meeting_point_ref_or_vehicle_meeting_point: Iterable[
        VehicleMeetingPointRef | VehicleMeetingPoint
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleMeetingPointRef",
                    "type": VehicleMeetingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPoint",
                    "type": VehicleMeetingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
