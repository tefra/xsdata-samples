from dataclasses import dataclass, field
from typing import Optional
from npo.models.match import Match

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MatcherList:
    class Meta:
        name = "matcherList"

    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
