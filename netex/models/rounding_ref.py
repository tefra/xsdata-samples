from dataclasses import dataclass
from netex.models.rounding_ref_structure import RoundingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoundingRef(RoundingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
