from dataclasses import dataclass, field
from typing import List
from netex.models.frame_containment_structure import FrameContainmentStructure
from netex.models.tariff import Tariff

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "tariffsInFrame_RelStructure"

    tariff: List[Tariff] = field(
        default_factory=list,
        metadata={
            "name": "Tariff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
