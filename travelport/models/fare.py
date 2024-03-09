from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class Fare:
    """
    Cruise Fare info.

    Parameters
    ----------
    fare_specific
        Category is fare specific or not
    multiple_fare_indicator
        Multiple fare are used or not
    rate_code
        Vendor defined rate code
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    fare_specific: None | bool = field(
        default=None,
        metadata={
            "name": "FareSpecific",
            "type": "Attribute",
        },
    )
    multiple_fare_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "MultipleFareIndicator",
            "type": "Attribute",
        },
    )
    rate_code: None | str = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
