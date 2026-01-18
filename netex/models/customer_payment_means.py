from __future__ import annotations

from dataclasses import dataclass

from .customer_payment_means_versioned_child_structure import (
    CustomerPaymentMeansVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPaymentMeans(CustomerPaymentMeansVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
