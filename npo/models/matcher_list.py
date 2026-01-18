from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.match import Match

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class MatcherList:
    class Meta:
        name = "matcherList"

    match: None | Match = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
