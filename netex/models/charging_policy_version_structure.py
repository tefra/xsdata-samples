from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .deposit_policy_enumeration import DepositPolicyEnumeration
from .travel_billing_policy_enumeration import TravelBillingPolicyEnumeration
from .travel_credit_policy_enumeration import TravelCreditPolicyEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ChargingPolicyVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "ChargingPolicy_VersionStructure"

    credit_policy: TravelCreditPolicyEnumeration | None = field(
        default=None,
        metadata={
            "name": "CreditPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    expire_after_period: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "ExpireAfterPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_grace_period: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "PaymentGracePeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    billing_policy: TravelBillingPolicyEnumeration | None = field(
        default=None,
        metadata={
            "name": "BillingPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deposit_policy: DepositPolicyEnumeration | None = field(
        default=None,
        metadata={
            "name": "DepositPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
