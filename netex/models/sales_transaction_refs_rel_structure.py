from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .sales_transaction_ref import SalesTransactionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesTransactionRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "salesTransactionRefs_RelStructure"

    sales_transaction_ref: Iterable[SalesTransactionRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
