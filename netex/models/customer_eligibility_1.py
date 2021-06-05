from dataclasses import dataclass
from netex.models.customer_eligibility_versioned_child_structure import CustomerEligibilityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerEligibility1(CustomerEligibilityVersionedChildStructure):
    class Meta:
        name = "CustomerEligibility"
        namespace = "http://www.netex.org.uk/netex"
