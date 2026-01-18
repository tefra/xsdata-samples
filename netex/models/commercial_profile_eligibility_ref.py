from __future__ import annotations

from dataclasses import dataclass

from .commercial_profile_eligibility_ref_structure import (
    CommercialProfileEligibilityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommercialProfileEligibilityRef(
    CommercialProfileEligibilityRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
