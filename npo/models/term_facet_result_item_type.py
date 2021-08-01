from dataclasses import dataclass, field
from typing import Optional
from npo.models.facet_result_item import FacetResultItem

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class TermFacetResultItemType(FacetResultItem):
    class Meta:
        name = "termFacetResultItemType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
