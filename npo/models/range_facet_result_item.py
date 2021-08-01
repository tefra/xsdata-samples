from dataclasses import dataclass, field
from typing import Optional
from npo.models.facet_result_item import FacetResultItem

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class RangeFacetResultItem(FacetResultItem):
    class Meta:
        name = "rangeFacetResultItem"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
