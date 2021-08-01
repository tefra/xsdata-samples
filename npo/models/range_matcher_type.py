from dataclasses import dataclass, field
from typing import Optional
from npo.models.match import Match

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class RangeMatcherType:
    class Meta:
        name = "rangeMatcherType"

    inclusive_end: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inclusiveEnd",
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
