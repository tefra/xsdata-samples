from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class FacetResultItem:
    class Meta:
        name = "facetResultItem"

    count: int = field(
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "required": True,
        }
    )
    selected: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
