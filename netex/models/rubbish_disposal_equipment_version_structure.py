from dataclasses import dataclass, field
from typing import Optional
from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RubbishDisposalEquipmentVersionStructure(
    PassengerEquipmentVersionStructure
):
    class Meta:
        name = "RubbishDisposalEquipment_VersionStructure"

    sharps_disposal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SharpsDisposal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    recycling: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Recycling",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
