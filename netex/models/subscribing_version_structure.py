from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from .payment_method_enumeration import PaymentMethodEnumeration
from .subscription_renewal_policy_enumeration import (
    SubscriptionRenewalPolicyEnumeration,
)
from .subscription_term_type_enumeration import SubscriptionTermTypeEnumeration
from .time_interval_refs_rel_structure import TimeIntervalRefsRelStructure
from .type_of_payment_method_refs_rel_structure import (
    TypeOfPaymentMethodRefsRelStructure,
)
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SubscribingVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Subscribing_VersionStructure"

    subscription_term_type: Optional[SubscriptionTermTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SubscriptionTermType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_subscription_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumSubscriptionPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_subscription_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumSubscriptionPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    subscription_renewal_policy: Optional[
        SubscriptionRenewalPolicyEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "SubscriptionRenewalPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    possible_installmentt_intervals: Optional[
        TimeIntervalRefsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "possibleInstallmenttIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    installment_payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "InstallmentPaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    installment_types_of_payment_method: Optional[
        TypeOfPaymentMethodRefsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "installmentTypesOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
