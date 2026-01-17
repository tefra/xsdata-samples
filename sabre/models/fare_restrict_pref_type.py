from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.prefer_level_type import PreferLevelType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class FareRestrictPrefType:
    """
    Identifies preferences for airfare restrictions acceptable or not
    acceptable for a given travel situation.

    Attributes:
        prefer_level:
        fare_restriction: Refer to OTA Code List Fare Restriction (FAR).
    """

    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        },
    )
    fare_restriction: None | str = field(
        default=None,
        metadata={
            "name": "FareRestriction",
            "type": "Attribute",
        },
    )
