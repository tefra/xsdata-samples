from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.models.travel_billing_policy_enumeration import TravelBillingPolicyEnumeration
from netex.models.travel_credit_policy_enumeration import TravelCreditPolicyEnumeration
from netex.models.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ChargingPolicyVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "ChargingPolicy_VersionStructure"

    credit_policy: Optional[TravelCreditPolicyEnumeration] = field(
        default=None,
        metadata={
            "name": "CreditPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    expire_after_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExpireAfterPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_grace_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PaymentGracePeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    billing_policy: Optional[TravelBillingPolicyEnumeration] = field(
        default=None,
        metadata={
            "name": "BillingPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
