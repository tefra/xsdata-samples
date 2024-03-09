from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.term_facet_result_item_type import TermFacetResultItemType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaGeoLocationFacetResultItemType(TermFacetResultItemType):
    class Meta:
        name = "mediaGeoLocationFacetResultItemType"

    term: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
