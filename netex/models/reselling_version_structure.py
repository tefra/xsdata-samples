from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDuration

from .effective_from_enumeration import EffectiveFromEnumeration
from .empty_type_2 import EmptyType2
from .payment_method_enumeration import PaymentMethodEnumeration
from .per_basis_enumeration import PerBasisEnumeration
from .resell_type_enumeration import ResellTypeEnumeration
from .resell_when_enumeration import ResellWhenEnumeration
from .time_interval_ref_structure import TimeIntervalRefStructure
from .type_of_payment_method_refs_rel_structure import (
    TypeOfPaymentMethodRefsRelStructure,
)
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResellingVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Reselling_VersionStructure"

    allowed: None | ResellTypeEnumeration = field(
        default=None,
        metadata={
            "name": "Allowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_change_class: None | bool = field(
        default=None,
        metadata={
            "name": "CanChangeClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    unused_tickets_only: None | bool = field(
        default=None,
        metadata={
            "name": "UnusedTicketsOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    only_at_certain_distribution_points: None | bool = field(
        default=None,
        metadata={
            "name": "OnlyAtCertainDistributionPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    resell_when: None | ResellWhenEnumeration = field(
        default=None,
        metadata={
            "name": "ResellWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    exchangable_from_any_time_or_exchangable_from_duration_or_exchangable_from_percent_use: (
        None | EmptyType2 | XmlDuration | Decimal
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExchangableFromAnyTime",
                    "type": EmptyType2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangableFromDuration",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangableFromPercentUse",
                    "type": Decimal,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    exchangable_from_interval_ref: None | TimeIntervalRefStructure = field(
        default=None,
        metadata={
            "name": "ExchangableFromIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    exchangable_until_any_time_or_exchangable_until_duration_or_exchangable_until_percent_use: (
        None | EmptyType2 | XmlDuration | Decimal
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExchangableUntilAnyTime",
                    "type": EmptyType2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangableUntilDuration",
                    "type": XmlDuration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangableUntilPercentUse",
                    "type": Decimal,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    exchangable_until_interval_ref: None | TimeIntervalRefStructure = field(
        default=None,
        metadata={
            "name": "ExchangableUntilIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    effective_from: None | EffectiveFromEnumeration = field(
        default=None,
        metadata={
            "name": "EffectiveFrom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notification_period: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "NotificationPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_fee: None | bool = field(
        default=None,
        metadata={
            "name": "HasFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    refund_basis: None | PerBasisEnumeration = field(
        default=None,
        metadata={
            "name": "RefundBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_methods: Iterable[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_payment_method_ref: None | TypeOfPaymentMethodRefsRelStructure = (
        field(
            default=None,
            metadata={
                "name": "typesOfPaymentMethodRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
