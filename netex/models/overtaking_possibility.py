from dataclasses import dataclass, field
from typing import Optional
from .overtaking_possibility_version_structure import (
    OvertakingPossibilityVersionStructure,
)
from .point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OvertakingPossibility(OvertakingPossibilityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    overtaking_at_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "OvertakingAtPointRef",
            "type": "Element",
            "required": True,
        },
    )
