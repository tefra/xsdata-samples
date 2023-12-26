from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.facet_result_item import FacetResultItem

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class TermFacetResultItemType(FacetResultItem):
    class Meta:
        name = "termFacetResultItemType"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
