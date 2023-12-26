from dataclasses import dataclass
from .entitlement_given_version_structure import (
    EntitlementGivenVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitlementGiven(EntitlementGivenVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
