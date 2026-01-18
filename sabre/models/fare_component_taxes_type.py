from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.air_tax_type import AirTaxType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class FareComponentTaxesType:
    """
    Attributes:
        flight_segment: A container for necessary data to describe one
            or more flight segments.
        tax: Any individual tax applied to the fare
    """

    flight_segment: list[FareComponentTaxesType.FlightSegment] = field(
        default_factory=list,
        metadata={
            "name": "FlightSegment",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        },
    )
    tax: list[AirTaxType] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 99,
        },
    )

    @dataclass(kw_only=True)
    class FlightSegment:
        """
        Attributes:
            departure_airport_code: Departure point of flight segment.
            arrival_airport_code: Arrival point of flight segment.
        """

        departure_airport_code: None | object = field(
            default=None,
            metadata={
                "name": "DepartureAirportCode",
                "type": "Attribute",
            },
        )
        arrival_airport_code: None | object = field(
            default=None,
            metadata={
                "name": "ArrivalAirportCode",
                "type": "Attribute",
            },
        )
