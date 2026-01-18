from __future__ import annotations

from dataclasses import dataclass

from npo.models.generic_media_search_result_type import (
    GenericMediaSearchResultType,
)

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class MediaSearchResultType(GenericMediaSearchResultType):
    class Meta:
        name = "mediaSearchResultType"
