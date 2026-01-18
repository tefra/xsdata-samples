from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.speed_percentile import SpeedPercentile
from datexii.models.eu.datexii.v2.speed_value import SpeedValue
from datexii.models.eu.datexii.v2.traffic_data import TrafficData

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TrafficSpeed(TrafficData):
    """
    Averaged measurements or calculations of traffic speed.

    :ivar average_vehicle_speed: An averaged measurement or calculation
        of the speed of vehicles at the specified location.
    :ivar speed_percentile:
    :ivar traffic_speed_extension:
    """

    average_vehicle_speed: SpeedValue | None = field(
        default=None,
        metadata={
            "name": "averageVehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    speed_percentile: SpeedPercentile | None = field(
        default=None,
        metadata={
            "name": "speedPercentile",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    traffic_speed_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "trafficSpeedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
