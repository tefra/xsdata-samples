from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.duration_value import DurationValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.floating_point_metre_distance_value import FloatingPointMetreDistanceValue
from datexii.models.eu.datexii.v2.traffic_data import TrafficData

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TrafficHeadway(TrafficData):
    """Averaged measurements or calculations of traffic headway, i.e. the distance
    or time interval between vehicles.

    This measure is measured from the head of one vehicle to the head of
    the following vehicle.

    :ivar average_distance_headway: The average distance between the
        front (respectively back) of this vehicle and the front
        (respectively  back) of the preceding vehicle, averaged for all
        vehicles within a defined measurement period at the specified
        measurement site.
    :ivar average_time_headway: The average time gap between the front
        (respectively back) of this vehicle and the front (respectively
        back) of the preceding vehicle, averaged for all vehicles within
        a defined measurement period at the specified measurement site.
    :ivar traffic_headway_extension:
    """
    average_distance_headway: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "averageDistanceHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    average_time_headway: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "averageTimeHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    traffic_headway_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficHeadwayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
