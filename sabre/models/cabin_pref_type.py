from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.cabin_type import CabinType
from sabre.models.prefer_level_type import PreferLevelType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class CabinPrefType:
    """
    Indicates preferences for choice of airline cabin for a given travel situation.

    Attributes:
        prefer_level:
        cabin: Specify cabin type.
    """

    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        },
    )
    cabin: None | CabinType = field(
        default=None,
        metadata={
            "name": "Cabin",
            "type": "Attribute",
        },
    )
