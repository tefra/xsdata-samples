from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_account_status import CustomerAccountStatus
from .customer_account_status_ref import CustomerAccountStatusRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfAccountStatusRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfAccountStatus_RelStructure"

    customer_account_status_ref: List[CustomerAccountStatusRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account_status: List[CustomerAccountStatus] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
