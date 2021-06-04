from dataclasses import dataclass
from netex.models.access_ref_structure import AccessRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRef(AccessRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
