from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class MaxLayoverDurationType:
    """User can specify its attribute's value in Minutes.

    Maximum size of each attribute is 4.

    Parameters
    ----------
    domestic
        It will be applied for all Domestic-to-Domestic connections.
    gateway
        It will be applied for all Domestic to International and
        International to Domestic connections.
    international
        It will be applied for all International-to-International
        connections.
    """

    domestic: None | int = field(
        default=None,
        metadata={
            "name": "Domestic",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 9999,
        },
    )
    gateway: None | int = field(
        default=None,
        metadata={
            "name": "Gateway",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 9999,
        },
    )
    international: None | int = field(
        default=None,
        metadata={
            "name": "International",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 9999,
        },
    )
