from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.flight_info_detail import FlightInfoDetail
from travelport.models.type_result_message_1 import TypeResultMessage1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlightInfo:
    """
    Parameters
    ----------
    flight_info_detail
    flight_info_error_message
        Errors, Warnings and informational messages for the Flight
        referenced above.
    criteria_key
        An identifier to link the flightinfo responses to the criteria in
        request. The value populated here is passed in request.
    carrier
        The carrier that is marketing this segment
    flight_number
        The flight number under which the marketing carrier is marketing
        this flight
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    departure_date
        The date at which this entity departs. This does not include time
        zone information since it can be derived from the origin location.
    class_of_service
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    flight_info_detail: list[FlightInfoDetail] = field(
        default_factory=list,
        metadata={
            "name": "FlightInfoDetail",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    flight_info_error_message: list[TypeResultMessage1] = field(
        default_factory=list,
        metadata={
            "name": "FlightInfoErrorMessage",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    criteria_key: None | str = field(
        default=None,
        metadata={
            "name": "CriteriaKey",
            "type": "Attribute",
            "required": True,
        }
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
            "required": True,
        }
    )
    class_of_service: None | str = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
