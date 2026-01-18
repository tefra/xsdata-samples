from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.direction_enum import DirectionEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_locations import GroupOfLocations
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.parking_route import ParkingRoute
from datexii.models.eu.datexii.v2.parking_route_direction_enum import (
    ParkingRouteDirectionEnum,
)
from datexii.models.eu.datexii.v2.parking_route_type_enum import (
    ParkingRouteTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class ParkingRouteDetails(ParkingRoute):
    """
    Urban context: Defining parking routes leading to the parking site.

    Truck parking context: Can be used to define a dynamic route
    management.

    :ivar parking_route_name: Name of the parking route.
    :ivar parking_route_type: The type of parking route. If not
        specified, the route is designed for any type of vehicles.
    :ivar dynamic_route_management: Indicates that there is dynamic
        route management for truck parking, i.e. a management system
        concerning several truck parkings (including this one) along a
        route.
    :ivar parking_route_icon_index: An index, which can identify some
        icon for visualisation of the route. Note that form and usage of
        this index as well as the icons itself are not further
        determined here.
    :ivar parking_route_direction: The direction of traffic, for which
        the parking route can be used. If not specified, the route can
        be used in the order of the given locations.
    :ivar parking_route_direction2: Additional directions of traffic,
        for which the parking route can be used. If not specified, the
        route can be used in the order of the given locations.
    :ivar group_of_locations:
    :ivar parking_route_details_extension:
    :ivar id:
    :ivar version:
    """

    parking_route_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "parkingRouteName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_route_type: None | ParkingRouteTypeEnum = field(
        default=None,
        metadata={
            "name": "parkingRouteType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dynamic_route_management: None | bool = field(
        default=None,
        metadata={
            "name": "dynamicRouteManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_route_icon_index: None | str = field(
        default=None,
        metadata={
            "name": "parkingRouteIconIndex",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    parking_route_direction: None | DirectionEnum = field(
        default=None,
        metadata={
            "name": "parkingRouteDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_route_direction2: None | ParkingRouteDirectionEnum = field(
        default=None,
        metadata={
            "name": "parkingRouteDirection2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_locations: None | GroupOfLocations = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_route_details_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "parkingRouteDetailsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
