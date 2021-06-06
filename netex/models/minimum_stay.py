from dataclasses import dataclass
from .minimum_stay_version_structure import MinimumStayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MinimumStay(MinimumStayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
