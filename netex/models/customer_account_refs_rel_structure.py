from collections.abc import Iterable
from dataclasses import dataclass, field

from .customer_account_ref import CustomerAccountRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerAccountRefs_RelStructure"

    customer_account_ref: Iterable[CustomerAccountRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
