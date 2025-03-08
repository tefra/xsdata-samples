from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.company_name_type import CompanyNameType
from sabre.models.response_location_type import ResponseLocationType
from sabre.models.rule_info_type import RuleInfoType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class FareInfoType:
    """
    Rules for this priced option.

    Attributes:
        departure_date: Departure Date for this priced fare.
        fare_reference: FareReferenceCode can be used for either the
            Fare Basis Code or the Fare Class Code.
        rule_info: Information regarding restrictions governing use of
            the fare.
        marketing_airline: The marketing airline.
        departure_airport: Departure point of flight segment.
        arrival_airport: Arrival point of flight segment.
        negotiated_fare: Indicator to show if this is a private fare.
        negotiated_fare_code: Code used to identify the private fare.
    """

    departure_date: None | str = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    fare_reference: None | str = field(
        default=None,
        metadata={
            "name": "FareReference",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        },
    )
    rule_info: None | RuleInfoType = field(
        default=None,
        metadata={
            "name": "RuleInfo",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    marketing_airline: list[CompanyNameType] = field(
        default_factory=list,
        metadata={
            "name": "MarketingAirline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    departure_airport: None | ResponseLocationType = field(
        default=None,
        metadata={
            "name": "DepartureAirport",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    arrival_airport: None | ResponseLocationType = field(
        default=None,
        metadata={
            "name": "ArrivalAirport",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    negotiated_fare: bool = field(
        default=False,
        metadata={
            "name": "NegotiatedFare",
            "type": "Attribute",
        },
    )
    negotiated_fare_code: None | str = field(
        default=None,
        metadata={
            "name": "NegotiatedFareCode",
            "type": "Attribute",
        },
    )
