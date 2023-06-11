from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.match import Match
from npo.models.owner_type_enum import OwnerTypeEnum
from npo.models.standard_match_type import StandardMatchType
from npo.models.textual_type_enum import TextualTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class TitleSearchType:
    class Meta:
        name = "titleSearchType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    owner: None | OwnerTypeEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type_value: None | TextualTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        }
    )
    match_type: None | StandardMatchType = field(
        default=None,
        metadata={
            "name": "matchType",
            "type": "Attribute",
        }
    )
    match: None | Match = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
