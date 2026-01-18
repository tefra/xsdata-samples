from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.car_park_configuration_enum import (
    CarParkConfigurationEnum,
)
from datexii.models.eu.datexii.v2.car_park_status_enum import CarParkStatusEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.non_road_event_information import (
    NonRoadEventInformation,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class CarParks(NonRoadEventInformation):
    """
    Provides information on the status of one or more car parks.

    :ivar car_park_configuration: The configuration/layout of a car
        park.
    :ivar car_park_identity: The identity of one or a group of car
        parks.
    :ivar car_park_occupancy: The percentage value of car parking spaces
        occupied.
    :ivar car_park_status: Indicates the status of one or more specified
        car parks.
    :ivar exit_rate: The rate at which vehicles are exiting the car
        park.
    :ivar fill_rate: The rate at which vehicles are entering the car
        park.
    :ivar number_of_vacant_parking_spaces: Indicates the number of
        vacant parking spaces available in a specified parking area.
    :ivar occupied_spaces: Number of currently occupied spaces.
    :ivar queuing_time: The current queuing time (duration) for entering
        the car park.
    :ivar total_capacity: Total number of car parking spaces.
    :ivar car_parks_extension:
    """

    car_park_configuration: CarParkConfigurationEnum | None = field(
        default=None,
        metadata={
            "name": "carParkConfiguration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    car_park_identity: str | None = field(
        default=None,
        metadata={
            "name": "carParkIdentity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    car_park_occupancy: float | None = field(
        default=None,
        metadata={
            "name": "carParkOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    car_park_status: CarParkStatusEnum | None = field(
        default=None,
        metadata={
            "name": "carParkStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    exit_rate: int | None = field(
        default=None,
        metadata={
            "name": "exitRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    fill_rate: int | None = field(
        default=None,
        metadata={
            "name": "fillRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    number_of_vacant_parking_spaces: int | None = field(
        default=None,
        metadata={
            "name": "numberOfVacantParkingSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    occupied_spaces: int | None = field(
        default=None,
        metadata={
            "name": "occupiedSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    queuing_time: float | None = field(
        default=None,
        metadata={
            "name": "queuingTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    total_capacity: int | None = field(
        default=None,
        metadata={
            "name": "totalCapacity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    car_parks_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "carParksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
