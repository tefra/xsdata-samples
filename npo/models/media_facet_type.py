from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.media_search_type import MediaSearchType
from npo.models.text_facet_type import TextFacetType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaFacetType(TextFacetType):
    class Meta:
        name = "mediaFacetType"

    filter: None | MediaSearchType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
