from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.duration_range_matcher_type import DurationRangeMatcherType
from npo.models.matcher_list import MatcherList

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class DurationRangeMatcherListType(MatcherList):
    class Meta:
        name = "durationRangeMatcherListType"

    matcher: list[DurationRangeMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
