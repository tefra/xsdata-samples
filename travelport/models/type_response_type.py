from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


class TypeResponseType(StrEnum):
    """
    Indicates the type of information to be returned in
    RailShopModifyAPIResponse.

    Values are “Schedules” or “Availability” or “Fares”. If not sent,
    “Fares” will be mapped if the request is for a specific rail segments,
    otherwise “Availability” will be mapped. Provider Supported RCH.
    """

    AVAILABILITY = "Availability"
    SCHEDULES = "Schedules"
    FARES = "Fares"
