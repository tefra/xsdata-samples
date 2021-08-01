from dataclasses import dataclass, field
from typing import List
from npo.models.duration_range_matcher_type import DurationRangeMatcherType
from npo.models.matcher_list import MatcherList

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DurationRangeMatcherListType(MatcherList):
    class Meta:
        name = "durationRangeMatcherListType"

    matcher: List[DurationRangeMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
