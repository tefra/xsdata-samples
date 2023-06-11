from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.term_facet_result_item_type import TermFacetResultItemType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class NamedTermFacetResultItemType:
    class Meta:
        name = "namedTermFacetResultItemType"

    facet: list[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
