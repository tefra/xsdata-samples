from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class NumTripsType:
    """
    This element allows a user to specify the number of itineraries
    returned.

    Attributes:
        number:
        per_date_min: Minimum number of options to be retrieved for each
            combination of outbound/inbound dates.
        per_date_max: Maximum number of options to be retrieved for each
            combination of outbound/inbound dates.
        per_market: Number of itineraries per market for alternate
            cities request. It allows to control market diversity only.
        per_month: In Advanced Calendar API: Maximum number of
            itineraries to be retrieved for each departure month and
            departure/arrival combination.
    """

    number: int = field(
        default=9,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    per_date_min: None | int = field(
        default=None,
        metadata={
            "name": "PerDateMin",
            "type": "Attribute",
        },
    )
    per_date_max: None | int = field(
        default=None,
        metadata={
            "name": "PerDateMax",
            "type": "Attribute",
        },
    )
    per_market: None | int = field(
        default=None,
        metadata={
            "name": "PerMarket",
            "type": "Attribute",
        },
    )
    per_month: None | int = field(
        default=None,
        metadata={
            "name": "PerMonth",
            "type": "Attribute",
        },
    )
