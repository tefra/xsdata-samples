from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.fare_note import FareNote
from travelport.models.type_ignore_stop_over import TypeIgnoreStopOver

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Connection:
    """
    Flight Connection Information.

    Parameters
    ----------
    fare_note
    change_of_plane
        Indicates the traveler must change planes between flights.
    change_of_terminal
        Indicates the traveler must change terminals between flights.
    change_of_airport
        Indicates the traveler must change airports between flights.
    stop_over
        Indicates that there is a significant delay between flights (usually
        12 hours or more)
    min_connection_time
        The minimum time needed to connect between the two different
        destinations.
    duration
        The actual duration (in minutes) between flights.
    segment_index
        The sequential AirSegment number that this connection information
        applies to.
    flight_details_index
        The sequential FlightDetails number that this connection information
        applies to.
    include_stop_over_to_fare_quote
        The field determines to quote fares with or without stop overs,the
        values can be NoStopOver,StopOver and IgnoreSegment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_note: None | FareNote = field(
        default=None,
        metadata={
            "name": "FareNote",
            "type": "Element",
        }
    )
    change_of_plane: bool = field(
        default=False,
        metadata={
            "name": "ChangeOfPlane",
            "type": "Attribute",
        }
    )
    change_of_terminal: bool = field(
        default=False,
        metadata={
            "name": "ChangeOfTerminal",
            "type": "Attribute",
        }
    )
    change_of_airport: bool = field(
        default=False,
        metadata={
            "name": "ChangeOfAirport",
            "type": "Attribute",
        }
    )
    stop_over: bool = field(
        default=False,
        metadata={
            "name": "StopOver",
            "type": "Attribute",
        }
    )
    min_connection_time: None | int = field(
        default=None,
        metadata={
            "name": "MinConnectionTime",
            "type": "Attribute",
        }
    )
    duration: None | int = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Attribute",
        }
    )
    segment_index: None | int = field(
        default=None,
        metadata={
            "name": "SegmentIndex",
            "type": "Attribute",
        }
    )
    flight_details_index: None | int = field(
        default=None,
        metadata={
            "name": "FlightDetailsIndex",
            "type": "Attribute",
        }
    )
    include_stop_over_to_fare_quote: None | TypeIgnoreStopOver = field(
        default=None,
        metadata={
            "name": "IncludeStopOverToFareQuote",
            "type": "Attribute",
        }
    )
