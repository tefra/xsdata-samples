from dataclasses import dataclass
from netex.models.submode_ref_structure import SubmodeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SubmodeRef(SubmodeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
