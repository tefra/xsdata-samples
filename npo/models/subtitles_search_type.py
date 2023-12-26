from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.match import Match
from npo.models.simple_matcher_type import SimpleMatcherType
from npo.models.text_matcher_list_type import TextMatcherListType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class SubtitlesSearchType:
    class Meta:
        name = "subtitlesSearchType"

    text: None | SimpleMatcherType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    mids: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    types: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    languages: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    match: None | Match = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
