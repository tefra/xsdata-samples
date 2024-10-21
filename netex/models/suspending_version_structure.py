from collections.abc import Iterable
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .suspension_policy_enumeration import SuspensionPolicyEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SuspendingVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Suspending_VersionStructure"

    suspension_policy: Iterable[SuspensionPolicyEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SuspensionPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    qualification_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "QualificationPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    qualification_percent: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "QualificationPercent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_suspension_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumSuspensionPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_suspension_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumSuspensionPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_suspensions_per_term: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfSuspensionsPerTerm",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
