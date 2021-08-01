from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class FacetResultItem:
    class Meta:
        name = "facetResultItem"

    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "required": True,
        }
    )
    selected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
