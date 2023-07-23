from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate, XmlTime
from travelport.models.connection import Connection
from travelport.models.type_days_of_operation import TypeDaysOfOperation

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlightTimeDetail:
    """
    Flight Time Table Response Details.

    Parameters
    ----------
    days_of_operation
    connection
    key
    vendor_code
    flight_number
    origin
    destination
    departure_time
        Flight departure time
    arrival_time
        Flight arrival time
    stop_count
    equipment
    schedule_start_date
        Flight time table search start date
    schedule_end_date
        Flight time table search end date
    display_option
        Indicates if carrier has link (carrier specific) display option.
    on_time_performance
        On time performance indicator in percentage.
    day_change
        Indicates if flight arrives on same day as departure, previous day,
        or next day. Like values  00 means Same day ,  01 means next day, -1
        mean Previous day etc.
    journey_time
        Indicates total journey time in minutes.
    flight_time
        Indicates total flight time in minutes.
    start_terminal
        Flight start terminal code.
    end_terminal
        Flight end terminal code.
    first_intermediate_stop
        First intermediate stop after board point.
    last_intermediate_stop
        Last intermediate stop before off point.
    inside_availability
    secure_sell
    availability_source
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    days_of_operation: None | TypeDaysOfOperation = field(
        default=None,
        metadata={
            "name": "DaysOfOperation",
            "type": "Element",
        }
    )
    connection: None | Connection = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Element",
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    vendor_code: None | str = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
        }
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
        }
    )
    departure_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        }
    )
    arrival_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    stop_count: None | int = field(
        default=None,
        metadata={
            "name": "StopCount",
            "type": "Attribute",
        }
    )
    equipment: None | str = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Attribute",
            "length": 3,
        }
    )
    schedule_start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ScheduleStartDate",
            "type": "Attribute",
        }
    )
    schedule_end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ScheduleEndDate",
            "type": "Attribute",
        }
    )
    display_option: None | bool = field(
        default=None,
        metadata={
            "name": "DisplayOption",
            "type": "Attribute",
        }
    )
    on_time_performance: None | int = field(
        default=None,
        metadata={
            "name": "OnTimePerformance",
            "type": "Attribute",
        }
    )
    day_change: None | int = field(
        default=None,
        metadata={
            "name": "DayChange",
            "type": "Attribute",
        }
    )
    journey_time: None | int = field(
        default=None,
        metadata={
            "name": "JourneyTime",
            "type": "Attribute",
        }
    )
    flight_time: None | int = field(
        default=None,
        metadata={
            "name": "FlightTime",
            "type": "Attribute",
        }
    )
    start_terminal: None | str = field(
        default=None,
        metadata={
            "name": "StartTerminal",
            "type": "Attribute",
        }
    )
    end_terminal: None | str = field(
        default=None,
        metadata={
            "name": "EndTerminal",
            "type": "Attribute",
        }
    )
    first_intermediate_stop: None | str = field(
        default=None,
        metadata={
            "name": "FirstIntermediateStop",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    last_intermediate_stop: None | str = field(
        default=None,
        metadata={
            "name": "LastIntermediateStop",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    inside_availability: None | str = field(
        default=None,
        metadata={
            "name": "InsideAvailability",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 1,
        }
    )
    secure_sell: None | str = field(
        default=None,
        metadata={
            "name": "SecureSell",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 2,
        }
    )
    availability_source: None | str = field(
        default=None,
        metadata={
            "name": "AvailabilitySource",
            "type": "Attribute",
            "max_length": 1,
        }
    )
