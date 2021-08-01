from dataclasses import dataclass, field
from typing import List
from npo.models.abstract_facet_type import AbstractFacetType
from npo.models.duration_range_facet_item_type import DurationRangeFacetItemType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DurationRangeFacetsType(AbstractFacetType):
    class Meta:
        name = "durationRangeFacetsType"

    interval: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "sequential": True,
        }
    )
    range: List[DurationRangeFacetItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "sequential": True,
        }
    )
