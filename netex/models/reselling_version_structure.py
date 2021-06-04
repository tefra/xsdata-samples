from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from netex.models.effective_from_enumeration import EffectiveFromEnumeration
from netex.models.empty_type_2 import EmptyType2
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.per_basis_enumeration import PerBasisEnumeration
from netex.models.resell_type_enumeration import ResellTypeEnumeration
from netex.models.resell_when_enumeration import ResellWhenEnumeration
from netex.models.time_interval_ref_structure import TimeIntervalRefStructure
from netex.models.type_of_payment_method_refs_rel_structure import TypeOfPaymentMethodRefsRelStructure
from netex.models.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResellingVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Reselling_VersionStructure"

    allowed: Optional[ResellTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "Allowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    can_change_class: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanChangeClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    unused_tickets_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnusedTicketsOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    only_at_certain_distribution_points: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnlyAtCertainDistributionPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    resell_when: Optional[ResellWhenEnumeration] = field(
        default=None,
        metadata={
            "name": "ResellWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchangable_from_any_time: Optional[EmptyType2] = field(
        default=None,
        metadata={
            "name": "ExchangableFromAnyTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchangable_from_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExchangableFromDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchangable_from_percent_use: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ExchangableFromPercentUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchangable_from_interval_ref: Optional[TimeIntervalRefStructure] = field(
        default=None,
        metadata={
            "name": "ExchangableFromIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchangable_until_any_time: Optional[EmptyType2] = field(
        default=None,
        metadata={
            "name": "ExchangableUntilAnyTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchangable_until_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExchangableUntilDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchangable_until_percent_use: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ExchangableUntilPercentUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchangable_until_interval_ref: Optional[TimeIntervalRefStructure] = field(
        default=None,
        metadata={
            "name": "ExchangableUntilIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    effective_from: Optional[EffectiveFromEnumeration] = field(
        default=None,
        metadata={
            "name": "EffectiveFrom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notification_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "NotificationPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    refund_basis: Optional[PerBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "RefundBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    types_of_payment_method_ref: Optional[TypeOfPaymentMethodRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
