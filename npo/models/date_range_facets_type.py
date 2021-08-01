from dataclasses import dataclass, field
from typing import List
from npo.models.abstract_facet_type import AbstractFacetType
from npo.models.date_range_facet_item_type import DateRangeFacetItemType
from npo.models.date_range_preset_type_enum import DateRangePresetTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DateRangeFacetsType(AbstractFacetType):
    class Meta:
        name = "dateRangeFacetsType"

    interval: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "sequential": True,
        }
    )
    preset: List[DateRangePresetTypeEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "sequential": True,
        }
    )
    range: List[DateRangeFacetItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "sequential": True,
        }
    )
