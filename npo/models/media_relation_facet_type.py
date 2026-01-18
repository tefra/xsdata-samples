from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.extended_media_facet_type import ExtendedMediaFacetType
from npo.models.media_relation_search_type import MediaRelationSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class MediaRelationFacetType(ExtendedMediaFacetType):
    class Meta:
        name = "mediaRelationFacetType"

    sub_search: None | MediaRelationSearchType = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
