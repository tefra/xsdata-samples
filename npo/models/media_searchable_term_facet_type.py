from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.media_facet_type import MediaFacetType
from npo.models.term_search_type import TermSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class MediaSearchableTermFacetType(MediaFacetType):
    class Meta:
        name = "mediaSearchableTermFacetType"

    sub_search: None | TermSearchType = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
