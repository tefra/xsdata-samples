from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.match import Match

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class RangeMatcherType:
    class Meta:
        name = "rangeMatcherType"

    inclusive_end: None | bool = field(
        default=None,
        metadata={
            "name": "inclusiveEnd",
            "type": "Attribute",
        },
    )
    match: None | Match = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
