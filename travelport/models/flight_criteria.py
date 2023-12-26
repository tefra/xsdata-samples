from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class FlightCriteria:
    """
    Search criterion for UniversalRecordPolicyDataReq.

    Parameters
    ----------
    value
    carrier
        Air segment carrier
    flight_number
        Air segment flight number
    departure_date
        AirSegment Departure date
    origin
        AirSegment Origin
    destination
        AirSegment destination
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
        },
    )
    departure_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
            "required": True,
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
