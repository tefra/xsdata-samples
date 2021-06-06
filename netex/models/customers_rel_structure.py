from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer import Customer
from .customer_ref import CustomerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "customers_RelStructure"

    customer_ref: List[CustomerRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer: List[Customer] = field(
        default_factory=list,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
