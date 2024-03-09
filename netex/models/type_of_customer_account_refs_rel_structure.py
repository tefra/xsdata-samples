from dataclasses import dataclass, field
from typing import List

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_customer_account_ref import TypeOfCustomerAccountRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfCustomerAccountRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfCustomerAccountRefs_RelStructure"

    type_of_customer_account_ref: List[TypeOfCustomerAccountRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfCustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
