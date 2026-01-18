from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.subtitles_search_type import SubtitlesSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class SubtitlesFormType:
    class Meta:
        name = "subtitlesFormType"

    searches: None | SubtitlesSearchType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
