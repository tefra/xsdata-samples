from dataclasses import dataclass, field
from typing import List
from netex.models.frame_containment_structure import FrameContainmentStructure
from netex.models.rounding import Rounding

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoundingsRelStructure(FrameContainmentStructure):
    class Meta:
        name = "roundings_RelStructure"

    rounding: List[Rounding] = field(
        default_factory=list,
        metadata={
            "name": "Rounding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
