from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class GroupOfParkingSitesTypeEnum(Enum):
    """
    The type of this group of parking sites.

    :cvar PARKING_AREA: A parking area in urban environment, for example
        all parkings sites in the western centre.
    :cvar TRUCK_PARKING_PRIORITY_ZONE: This group is describing a truck
        parking priority zone according to the EU regulation.
    :cvar AGGREGATION_OF_INFORMATION: The main purpose of this group is
        to give summarized information of all encapsulated parking sites
        (e.g. number of spaces in total).
    :cvar INHABITANT_ZONE: This group is describing an inhabitant zone.
    """

    PARKING_AREA = "parkingArea"
    TRUCK_PARKING_PRIORITY_ZONE = "truckParkingPriorityZone"
    AGGREGATION_OF_INFORMATION = "aggregationOfInformation"
    INHABITANT_ZONE = "inhabitantZone"
