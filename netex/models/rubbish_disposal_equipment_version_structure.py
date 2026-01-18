from __future__ import annotations

from dataclasses import dataclass, field

from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RubbishDisposalEquipmentVersionStructure(
    PassengerEquipmentVersionStructure
):
    class Meta:
        name = "RubbishDisposalEquipment_VersionStructure"

    sharps_disposal: None | bool = field(
        default=None,
        metadata={
            "name": "SharpsDisposal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    recycling: None | bool = field(
        default=None,
        metadata={
            "name": "Recycling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
