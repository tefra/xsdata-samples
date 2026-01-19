from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration, XmlTime

from .purchase_action_enumeration import PurchaseActionEnumeration
from .purchase_moment_enumeration import PurchaseMomentEnumeration
from .purchase_when_enumeration import PurchaseWhenEnumeration
from .time_interval_ref_structure import TimeIntervalRefStructure
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurchaseWindowVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "PurchaseWindow_VersionStructure"

    purchase_action: None | PurchaseActionEnumeration = field(
        default=None,
        metadata={
            "name": "PurchaseAction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    purchase_when: None | PurchaseWhenEnumeration = field(
        default=None,
        metadata={
            "name": "PurchaseWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    latest_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "LatestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_period_before_departure: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MinimumPeriodBeforeDeparture",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_period_interval_ref: None | TimeIntervalRefStructure = field(
        default=None,
        metadata={
            "name": "MinimumPeriodIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_period_before_departure: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MaximumPeriodBeforeDeparture",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_period_interval_ref: None | TimeIntervalRefStructure = field(
        default=None,
        metadata={
            "name": "MaximumPeriodIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    purchase_moment: Sequence[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseMoment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
