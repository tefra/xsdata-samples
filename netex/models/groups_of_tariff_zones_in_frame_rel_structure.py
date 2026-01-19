from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_tariff_zones import GroupOfTariffZones

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfTariffZonesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfTariffZonesInFrame_RelStructure"

    group_of_tariff_zones: Sequence[GroupOfTariffZones] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
