from dataclasses import dataclass, field
from typing import Optional
from npo.models.media_search_type import MediaSearchType
from npo.models.text_facet_type import TextFacetType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ExtendedMediaFacetType(TextFacetType):
    class Meta:
        name = "extendedMediaFacetType"

    filter: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    case_sensitive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "caseSensitive",
            "type": "Attribute",
        }
    )
