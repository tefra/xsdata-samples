from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .charging_equipment_profile import ChargingEquipmentProfile
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingEquipmenProfilesInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "chargingEquipmenProfilesInFrame_RelStructure"

    charging_equipment_profile: Iterable[ChargingEquipmentProfile] = field(
        default_factory=list,
        metadata={
            "name": "ChargingEquipmentProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
