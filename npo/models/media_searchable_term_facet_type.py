from dataclasses import dataclass, field
from typing import Optional
from npo.models.media_facet_type import MediaFacetType
from npo.models.term_search_type import TermSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaSearchableTermFacetType(MediaFacetType):
    class Meta:
        name = "mediaSearchableTermFacetType"

    sub_search: Optional[TermSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
