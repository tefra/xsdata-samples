from dataclasses import dataclass
from netex.models.interchanging_ref_structure import InterchangingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangingRef(InterchangingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
