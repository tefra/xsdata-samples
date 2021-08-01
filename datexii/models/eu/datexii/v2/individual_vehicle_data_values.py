from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.date_time_value import DateTimeValue
from datexii.models.eu.datexii.v2.duration_value import DurationValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.floating_point_metre_distance_value import FloatingPointMetreDistanceValue
from datexii.models.eu.datexii.v2.speed_value import SpeedValue
from datexii.models.eu.datexii.v2.traffic_data import TrafficData

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class IndividualVehicleDataValues(TrafficData):
    """
    Measured or calculated data values relating to individual vehicles derived
    from detectors at the specified measurement site.

    :ivar individual_vehicle_speed: The measured speed of the individual
        vehicle at the specified measurement site.
    :ivar arrival_time: The time of the arrival of an individual vehicle
        in a detection zone.
    :ivar exit_time: The time when an individual vehicle leaves a
        detection zone.
    :ivar passage_duration_time: The time elapsed between an individual
        vehicle entering a detection zone and exiting the same detection
        zone as detected by entry and exit sensors.
    :ivar presence_duration_time: The period of time during which a
        vehicle activates a presence sensor.
    :ivar time_gap: The time interval between the arrival of this
        vehicle's front at a point on the roadway, and that of the
        departure of the rear of the preceding one.
    :ivar time_headway: The measured time interval between this
        vehicle's arrival at (or departure from) a point on the roadway,
        and that of the preceding one.
    :ivar distance_gap: The measured distance between the front of this
        vehicle and the rear of the preceding one, in metres at the
        specified measurement site.
    :ivar distance_headway: The measured distance between the front
        (respectively back) of this vehicle and the front (respectively
        back) of the preceding vehicle at the specified measurement
        site.
    :ivar individual_vehicle_data_values_extension:
    """
    individual_vehicle_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "individualVehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    arrival_time: Optional[DateTimeValue] = field(
        default=None,
        metadata={
            "name": "arrivalTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    exit_time: Optional[DateTimeValue] = field(
        default=None,
        metadata={
            "name": "exitTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    passage_duration_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "passageDurationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    presence_duration_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "presenceDurationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    time_gap: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "timeGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    time_headway: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "timeHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_gap: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "distanceGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_headway: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "distanceHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    individual_vehicle_data_values_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "individualVehicleDataValuesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
