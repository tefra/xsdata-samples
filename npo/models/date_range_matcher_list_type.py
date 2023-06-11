from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.date_range_matcher_type import DateRangeMatcherType
from npo.models.matcher_list import MatcherList

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DateRangeMatcherListType(MatcherList):
    class Meta:
        name = "dateRangeMatcherListType"

    matcher: list[DateRangeMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
