from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.hightlight_type import HightlightType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class SearchResultItem:
    class Meta:
        name = "searchResultItem"

    result: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    highlight: list[HightlightType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    score: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
