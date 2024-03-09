from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.facet_result_item import FacetResultItem

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class RangeFacetResultItem(FacetResultItem):
    class Meta:
        name = "rangeFacetResultItem"

    value: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
