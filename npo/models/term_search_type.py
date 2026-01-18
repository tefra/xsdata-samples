from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.match import Match
from npo.models.text_matcher_list_type import TextMatcherListType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class TermSearchType:
    class Meta:
        name = "termSearchType"

    ids: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    match: None | Match = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
