from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class OfferAvailabilityModifiers:
    """
    Parameters
    ----------
    service_type
        To restrict offers to only this type.
    carrier
        The carrier whose paid seat optional services is to be returned by
        uAPI.
    currency_type
        Currency code override. Providers: ACH, 1G, 1V, 1P
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    service_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ServiceType",
            "type": "Element",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 128,
        }
    )
    carrier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "max_occurs": 999,
            "length": 2,
        }
    )
    currency_type: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "length": 3,
        }
    )
