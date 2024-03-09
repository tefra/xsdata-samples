from dataclasses import dataclass

from .customer_eligibility_ref_structure import CustomerEligibilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerEligibilityRef(CustomerEligibilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
