from dataclasses import dataclass
from netex.models.customer_ref_structure import CustomerRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerRef(CustomerRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
