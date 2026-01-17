from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRuleKey:
    """
    The Fare Rule requested using a Key.

    The key is typically a provider specific string which is required to
    make a following Air Fare Rule Request. This Key is returned in Low
    Fare Shop or Air Price Response.

    Parameters
    ----------
    value
    fare_info_ref
        The Fare Component to which this Rule Key applies
    provider_code
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
        },
    )
    fare_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
            "required": True,
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
