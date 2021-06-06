from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_account import CustomerAccount
from .customer_account_ref import CustomerAccountRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "customerAccounts_RelStructure"

    customer_account_ref: List[CustomerAccountRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account: List[CustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
