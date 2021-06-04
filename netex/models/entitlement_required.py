from dataclasses import dataclass
from netex.models.entitlement_required_version_structure import EntitlementRequiredVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitlementRequired(EntitlementRequiredVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
