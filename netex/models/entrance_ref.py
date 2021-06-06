from dataclasses import dataclass
from .entrance_ref_structure import EntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntranceRef(EntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
