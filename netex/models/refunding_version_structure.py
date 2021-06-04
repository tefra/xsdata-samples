from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.partial_refund_basis_enumeration import PartialRefundBasisEnumeration
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.refund_policy_enumeration import RefundPolicyEnumeration
from netex.models.refund_type_enumeration import RefundTypeEnumeration
from netex.models.reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RefundingVersionStructure(ResellingVersionStructure):
    class Meta:
        name = "Refunding_VersionStructure"

    refund_type: Optional[RefundTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RefundType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    refund_policy: List[RefundPolicyEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RefundPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    partial_refund_basis: Optional[PartialRefundBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "PartialRefundBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_method: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
