from __future__ import annotations

from dataclasses import dataclass, field

from .on_becoming_enumeration import OnBecomingEnumeration
from .on_ceasing_enumeration import OnCeasingEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EligibilityChangePolicyVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "EligibilityChangePolicy_VersionStructure"

    on_becoming_eligible_policy: None | OnBecomingEnumeration = field(
        default=None,
        metadata={
            "name": "OnBecomingEligiblePolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    on_ceasing_to_be_eligible_policy: None | OnCeasingEnumeration = field(
        default=None,
        metadata={
            "name": "OnCeasingToBeEligiblePolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
