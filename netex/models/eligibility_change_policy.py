from __future__ import annotations

from dataclasses import dataclass

from .eligibility_change_policy_version_structure import (
    EligibilityChangePolicyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EligibilityChangePolicy(EligibilityChangePolicyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
