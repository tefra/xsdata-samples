from dataclasses import dataclass, field
from typing import List
from npo.models.date_range_matcher_type import DateRangeMatcherType
from npo.models.matcher_list import MatcherList

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DateRangeMatcherListType(MatcherList):
    class Meta:
        name = "dateRangeMatcherListType"

    matcher: List[DateRangeMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
