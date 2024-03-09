from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.basic_data import BasicData
from datexii.models.eu.datexii.v2.duration_value import DurationValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.speed_value import SpeedValue
from datexii.models.eu.datexii.v2.travel_time_trend_type_enum import (
    TravelTimeTrendTypeEnum,
)
from datexii.models.eu.datexii.v2.travel_time_type_enum import (
    TravelTimeTypeEnum,
)
from datexii.models.eu.datexii.v2.vehicle_type_enum import VehicleTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TravelTimeData(BasicData):
    """
    Derived/computed travel time information relating to a linear section of the
    road network; forecast = true means a forecast for a vehicle at the start of
    the specified location, forecast = false means calculation/measurement at the
    end.

    :ivar travel_time_trend_type: The current trend in the travel time
        between the defined locations in the specified direction.
    :ivar travel_time_type: Indication of the way in which the travel
        time is derived.
    :ivar vehicle_type: Vehicle type.
    :ivar travel_time: Derived/computed travel time information relating
        to a specific group of locations.
    :ivar free_flow_travel_time: The travel time which would be expected
        under ideal free flow conditions.
    :ivar normally_expected_travel_time: The travel time which is
        expected for the given period (e.g. date/time, holiday status
        etc.) and any known quasi-static conditions (e.g. long term
        roadworks). This value is derived from historical analysis.
    :ivar free_flow_speed: The free flow speed expected under ideal
        conditions, corresponding to the freeFlowTravelTime.
    :ivar travel_time_data_extension:
    """

    travel_time_trend_type: Optional[TravelTimeTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "travelTimeTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    travel_time_type: Optional[TravelTimeTypeEnum] = field(
        default=None,
        metadata={
            "name": "travelTimeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_type: List[VehicleTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "vehicleType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    travel_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "travelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    free_flow_travel_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "freeFlowTravelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    normally_expected_travel_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "normallyExpectedTravelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    free_flow_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "freeFlowSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    travel_time_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "travelTimeDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
