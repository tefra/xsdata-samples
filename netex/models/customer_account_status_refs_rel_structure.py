from dataclasses import dataclass, field
from typing import List

from .customer_account_status_ref import CustomerAccountStatusRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountStatusRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerAccountStatusRefs_RelStructure"

    customer_account_status_ref: List[CustomerAccountStatusRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
