from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .partial_refund_basis_enumeration import PartialRefundBasisEnumeration
from .payment_method_enumeration import PaymentMethodEnumeration
from .refund_policy_enumeration import RefundPolicyEnumeration
from .refund_type_enumeration import RefundTypeEnumeration
from .reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RefundingVersionStructure(ResellingVersionStructure):
    class Meta:
        name = "Refunding_VersionStructure"

    refund_type: None | RefundTypeEnumeration = field(
        default=None,
        metadata={
            "name": "RefundType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    refund_policy: Iterable[RefundPolicyEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RefundPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    partial_refund_basis: None | PartialRefundBasisEnumeration = field(
        default=None,
        metadata={
            "name": "PartialRefundBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_method: Iterable[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
