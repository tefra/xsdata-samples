from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_customer_account import TypeOfCustomerAccount
from .type_of_customer_account_ref import TypeOfCustomerAccountRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfCustomerAccountRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfCustomerAccount_RelStructure"

    type_of_customer_account_ref: List[TypeOfCustomerAccountRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_customer_account: List[TypeOfCustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
