from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from sabre.models.processing_message_type import ProcessingMessageType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class OneWayProcessingMessageType(ProcessingMessageType):
    """
    Attributes:
        departure_date: Departure date
        departure_airport: Location identifying code.
        arrival_airport: Location identifying code.
    """

    departure_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        },
    )
    departure_airport: None | str = field(
        default=None,
        metadata={
            "name": "DepartureAirport",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
    arrival_airport: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalAirport",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
