from dataclasses import dataclass
from netex.models.minimum_stay_ref_structure import MinimumStayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MinimumStayRef(MinimumStayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
