from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.match import Match
from npo.models.standard_match_type import StandardMatchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ExtendedMatcherType:
    class Meta:
        name = "extendedMatcherType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    fuzziness: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    match_type: None | StandardMatchType = field(
        default=None,
        metadata={
            "name": "matchType",
            "type": "Attribute",
        },
    )
    case_sensitive: None | bool = field(
        default=None,
        metadata={
            "name": "caseSensitive",
            "type": "Attribute",
        },
    )
    match: None | Match = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
