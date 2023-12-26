from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BrandInfo:
    """
    Commercially recognized product offered by an airline.

    Parameters
    ----------
    key
        Brand Key
    brand_id
        The unique identifier of the brand
    air_pricing_info_ref
        A reference to a AirPricing. Providers: ACH, 1G, 1V, 1P.
    fare_info_ref
        A reference to a FareInfo. Providers: ACH, 1G, 1V, 1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    brand_id: None | str = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 19,
        },
    )
    air_pricing_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Attribute",
        },
    )
    fare_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
        },
    )
