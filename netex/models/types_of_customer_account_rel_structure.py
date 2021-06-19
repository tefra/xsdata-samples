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

    type_of_customer_account_ref_or_type_of_customer_account: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfCustomerAccountRef",
                    "type": TypeOfCustomerAccountRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCustomerAccount",
                    "type": TypeOfCustomerAccount,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
