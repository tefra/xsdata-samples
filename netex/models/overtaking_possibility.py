from dataclasses import dataclass
from .overtaking_possibility_version_structure import OvertakingPossibilityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OvertakingPossibility(OvertakingPossibilityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
