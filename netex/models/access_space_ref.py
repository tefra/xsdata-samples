from dataclasses import dataclass
from netex.models.access_space_ref_structure import AccessSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessSpaceRef(AccessSpaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
