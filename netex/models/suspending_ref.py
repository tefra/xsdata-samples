from dataclasses import dataclass

from .suspending_ref_structure import SuspendingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SuspendingRef(SuspendingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
