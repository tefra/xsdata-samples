from dataclasses import dataclass
from netex.models.mode_ref_structure import ModeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ModeRef(ModeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
