from dataclasses import dataclass
from netex.models.customer_account_status_ref_structure import CustomerAccountStatusRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountStatusRef(CustomerAccountStatusRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
