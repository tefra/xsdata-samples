from dataclasses import dataclass
from .reserving_ref_structure import ReservingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReservingRef(ReservingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
