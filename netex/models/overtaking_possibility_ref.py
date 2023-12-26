from dataclasses import dataclass
from .overtaking_possibility_ref_structure import (
    OvertakingPossibilityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OvertakingPossibilityRef(OvertakingPossibilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
