from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class OcfeeType:
    """
    OC Fee details.

    Attributes:
        amount: Fee amount
        description: Fee description
        origin_airport: Origin airport
        destination_airport: Destination airport
        carrier: Operating carrier code
        passenger_code: Ancillary fee code
        date: Date for this fee.
        start_segment: Start travel segment
        end_segment: End travel segment
    """

    class Meta:
        name = "OCFeeType"

    amount: None | Decimal = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
            "fraction_digits": 3,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
    origin_airport: None | str = field(
        default=None,
        metadata={
            "name": "OriginAirport",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        },
    )
    destination_airport: None | str = field(
        default=None,
        metadata={
            "name": "DestinationAirport",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        },
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        },
    )
    passenger_code: None | str = field(
        default=None,
        metadata={
            "name": "PassengerCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9]{2,3}",
        },
    )
    date: None | str = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Attribute",
        },
    )
    start_segment: None | object = field(
        default=None,
        metadata={
            "name": "StartSegment",
            "type": "Attribute",
            "required": True,
        },
    )
    end_segment: None | object = field(
        default=None,
        metadata={
            "name": "EndSegment",
            "type": "Attribute",
            "required": True,
        },
    )
