from dataclasses import dataclass

from .replacing_ref_structure import ReplacingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReplacingRef(ReplacingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
