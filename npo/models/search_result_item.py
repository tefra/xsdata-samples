from dataclasses import dataclass, field
from typing import List, Optional
from npo.models.hightlight_type import HightlightType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class SearchResultItem:
    class Meta:
        name = "searchResultItem"

    result: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: List[HightlightType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    score: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
