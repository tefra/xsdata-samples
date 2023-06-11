from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.match import Match
from npo.models.simple_match_type import SimpleMatchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class SimpleMatcherType:
    class Meta:
        name = "simpleMatcherType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    fuzziness: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match_type: None | SimpleMatchType = field(
        default=None,
        metadata={
            "name": "matchType",
            "type": "Attribute",
        }
    )
    match: None | Match = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
