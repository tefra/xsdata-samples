from dataclasses import dataclass
from .customer_account_status_version_structure import CustomerAccountStatusVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountStatus(CustomerAccountStatusVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
