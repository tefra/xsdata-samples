from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.abstract_facet_type import AbstractFacetType
from npo.models.date_range_facet_item_type import DateRangeFacetItemType
from npo.models.date_range_preset_type_enum import DateRangePresetTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DateRangeFacetsType(AbstractFacetType):
    class Meta:
        name = "dateRangeFacetsType"

    interval: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    preset: list[DateRangePresetTypeEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    range: list[DateRangeFacetItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
