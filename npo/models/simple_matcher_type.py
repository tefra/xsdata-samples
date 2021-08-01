from dataclasses import dataclass, field
from typing import Optional
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
    fuzziness: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match_type: Optional[SimpleMatchType] = field(
        default=None,
        metadata={
            "name": "matchType",
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
