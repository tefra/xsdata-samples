from dataclasses import dataclass
from .customer_eligibility_versioned_child_structure import CustomerEligibilityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerEligibility(CustomerEligibilityVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
