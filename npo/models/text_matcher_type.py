from dataclasses import dataclass, field
from typing import Optional
from npo.models.match import Match
from npo.models.standard_match_type import StandardMatchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class TextMatcherType:
    class Meta:
        name = "textMatcherType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    match_type: Optional[StandardMatchType] = field(
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
