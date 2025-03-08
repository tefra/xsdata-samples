from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.company_name_type import CompanyNameType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class OperatingAirlineType(CompanyNameType):
    """
    This is an extension of CompanyNameType to include a FlightNumber.
    """

    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "pattern": r"[0-9]{1,4}[A-Z]?",
        },
    )
