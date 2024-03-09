from dataclasses import dataclass
from .entity_in_version_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerEligibility2(VersionedChildStructure):
    class Meta:
        name = "CustomerEligibility_"
        namespace = "http://www.netex.org.uk/netex"
