from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.abstract_facet_type import AbstractFacetType
from npo.models.duration_range_facet_item_type import (
    DurationRangeFacetItemType,
)

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class DurationRangeFacetsType(AbstractFacetType):
    class Meta:
        name = "durationRangeFacetsType"

    interval: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    range: list[DurationRangeFacetItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
