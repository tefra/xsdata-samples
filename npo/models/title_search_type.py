from dataclasses import dataclass, field
from typing import Optional
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
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match_type: Optional[StandardMatchType] = field(
        default=None,
        metadata={
            "name": "matchType",
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
