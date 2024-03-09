from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

from travelport.models.carrier_list import CarrierList
from travelport.models.type_days_of_operation import TypeDaysOfOperation
from travelport.models.type_location_1 import TypeLocation1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class GeneralTimeTable:
    """
    Parameters
    ----------
    days_of_operation
    flight_origin
    flight_destination
    carrier_list
    start_date
    end_date
    start_time
        Flight start time of flight time tabel .
    end_time
        Flight end time of flight time tabel .
    include_connection
        Include or exclude connecting flights.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    days_of_operation: None | TypeDaysOfOperation = field(
        default=None,
        metadata={
            "name": "DaysOfOperation",
            "type": "Element",
        },
    )
    flight_origin: None | TypeLocation1 = field(
        default=None,
        metadata={
            "name": "FlightOrigin",
            "type": "Element",
            "required": True,
        },
    )
    flight_destination: None | TypeLocation1 = field(
        default=None,
        metadata={
            "name": "FlightDestination",
            "type": "Element",
            "required": True,
        },
    )
    carrier_list: None | CarrierList = field(
        default=None,
        metadata={
            "name": "CarrierList",
            "type": "Element",
        },
    )
    start_date: None | str = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        },
    )
    end_date: None | str = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        },
    )
    start_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Attribute",
        },
    )
    end_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Attribute",
        },
    )
    include_connection: None | bool = field(
        default=None,
        metadata={
            "name": "IncludeConnection",
            "type": "Attribute",
        },
    )
