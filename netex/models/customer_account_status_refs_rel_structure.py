from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .customer_account_status_ref import CustomerAccountStatusRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountStatusRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerAccountStatusRefs_RelStructure"

    customer_account_status_ref: Iterable[CustomerAccountStatusRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountStatusRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
