from __future__ import annotations

from dataclasses import dataclass

from .eligibility_change_policy_ref_structure import (
    EligibilityChangePolicyRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EligibilityChangePolicyRef(EligibilityChangePolicyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
