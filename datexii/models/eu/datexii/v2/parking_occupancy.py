from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.parking_occupancy_enum import (
    ParkingOccupancyEnum,
)
from datexii.models.eu.datexii.v2.parking_occupancy_trend_enum import (
    ParkingOccupancyTrendEnum,
)
from datexii.models.eu.datexii.v2.parking_vacant_spaces_enum import (
    ParkingVacantSpacesEnum,
)
from datexii.models.eu.datexii.v2.vehicle_count_and_rate import (
    VehicleCountAndRate,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingOccupancy:
    """
    Parking capacity information for the parking site as well as for
    AssignedParkingSpaces.

    :ivar parking_number_of_spaces_override: Possibility to override the
        static value 'parkingNumberOfSpaces'.
    :ivar parking_number_of_vacant_spaces: The total number of currently
        vacant parking spaces available in the specified parking site,
        group of parking sites or group of parking spaces.
    :ivar parking_number_of_vacant_spaces_lower_than: The number of
        vacant parking spaces is lower than the given value (example:
        Less than 10 spaces are free).
    :ivar parking_number_of_vacant_spaces_higher_than: The number of
        vacant parking spaces is higher than the given value (example:
        More than 10 spaces are free).
    :ivar parking_number_of_vacant_spaces_graded: Number of vacant
        spaces by grading (enumeration).
    :ivar parking_number_of_occupied_spaces: The number of currently
        occupied spaces in the specified parking site, group of parking
        sites or assigned parking.
    :ivar parking_number_of_vehicles: Number of vehicles (of specified
        type) on the parking site, the group of parking sites or the
        group of parking spaces. Parking too narrow or too wide may
        effect differences to the 'occupiedSpaces' value. Should not
        include petrol station traffic.
    :ivar parking_occupancy: The percentage value of parking spaces
        occupied in the specified parking site, group of parking sites
        or assigned parking.
    :ivar parking_occupancy_graded: Occupied parking spaces by a
        percentage-grading (enumeration).
    :ivar parking_occupancy_trend: The trend of the occupancy of the
        parking spaces in the specified parking site, group of parking
        sites or assigned parking.
    :ivar parking_not_allowed: In case of 'true', parking is not allowed
        (e.g. abnormal closure).
    :ivar vehicle_count_and_rate:
    :ivar parking_occupancy_extension:
    """

    parking_number_of_spaces_override: None | int = field(
        default=None,
        metadata={
            "name": "parkingNumberOfSpacesOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_number_of_vacant_spaces: None | int = field(
        default=None,
        metadata={
            "name": "parkingNumberOfVacantSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_number_of_vacant_spaces_lower_than: None | int = field(
        default=None,
        metadata={
            "name": "parkingNumberOfVacantSpacesLowerThan",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_number_of_vacant_spaces_higher_than: None | int = field(
        default=None,
        metadata={
            "name": "parkingNumberOfVacantSpacesHigherThan",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_number_of_vacant_spaces_graded: None | ParkingVacantSpacesEnum = (
        field(
            default=None,
            metadata={
                "name": "parkingNumberOfVacantSpacesGraded",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    parking_number_of_occupied_spaces: None | int = field(
        default=None,
        metadata={
            "name": "parkingNumberOfOccupiedSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_number_of_vehicles: None | int = field(
        default=None,
        metadata={
            "name": "parkingNumberOfVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_occupancy: None | float = field(
        default=None,
        metadata={
            "name": "parkingOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_occupancy_graded: None | ParkingOccupancyEnum = field(
        default=None,
        metadata={
            "name": "parkingOccupancyGraded",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_occupancy_trend: None | ParkingOccupancyTrendEnum = field(
        default=None,
        metadata={
            "name": "parkingOccupancyTrend",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_not_allowed: None | bool = field(
        default=None,
        metadata={
            "name": "parkingNotAllowed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_count_and_rate: list[VehicleCountAndRate] = field(
        default_factory=list,
        metadata={
            "name": "vehicleCountAndRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_occupancy_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "parkingOccupancyExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
