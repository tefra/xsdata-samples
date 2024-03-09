from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SponsoredFltInfo:
    """This describes whether the segment is determined to be a sponsored flight.

    The SponsoredFltInfo node will only come back for Travelport UIs and
    not for other customers.

    Parameters
    ----------
    sponsored_lnb
        The line number of the sponsored flight item
    neutral_lnb
        The neutral line number for the flight item.
    flt_key
        The unique identifying key for the sponsored flight.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    sponsored_lnb: None | int = field(
        default=None,
        metadata={
            "name": "SponsoredLNB",
            "type": "Attribute",
            "required": True,
        },
    )
    neutral_lnb: None | int = field(
        default=None,
        metadata={
            "name": "NeutralLNB",
            "type": "Attribute",
            "required": True,
        },
    )
    flt_key: None | str = field(
        default=None,
        metadata={
            "name": "FltKey",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        },
    )
