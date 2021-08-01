from dataclasses import dataclass, field
from typing import Optional
from npo.models.subtitles_search_type import SubtitlesSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class SubtitlesFormType:
    class Meta:
        name = "subtitlesFormType"

    searches: Optional[SubtitlesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
