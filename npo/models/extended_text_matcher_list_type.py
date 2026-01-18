from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.extended_matcher_type import ExtendedMatcherType
from npo.models.matcher_list import MatcherList

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class ExtendedTextMatcherListType(MatcherList):
    class Meta:
        name = "extendedTextMatcherListType"

    matcher: list[ExtendedMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
