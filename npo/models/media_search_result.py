from __future__ import annotations
from dataclasses import dataclass
from npo.models.media_search_result_type import MediaSearchResultType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaSearchResult(MediaSearchResultType):
    class Meta:
        name = "mediaSearchResult"
        namespace = "urn:vpro:api:2013"
