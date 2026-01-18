from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
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
    carrier: str = field(
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    flight_number: str = field(
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    departure_date: XmlDate = field(
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
            "required": True,
        }
    )
    origin: str = field(
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: str = field(
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
