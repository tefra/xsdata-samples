from dataclasses import dataclass
from netex.models.entitlement_required_ref_structure import EntitlementRequiredRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitlementRequiredRef(EntitlementRequiredRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
