from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .customer_payment_means_ref import CustomerPaymentMeansRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPaymentMeanRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerPaymentMeanRefs_RelStructure"

    customer_payment_means_ref: Iterable[CustomerPaymentMeansRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPaymentMeansRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
