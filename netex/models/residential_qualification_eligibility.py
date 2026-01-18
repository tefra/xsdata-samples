from __future__ import annotations

from dataclasses import dataclass

from .residential_qualification_eligibility_versioned_child_structure import (
    ResidentialQualificationEligibilityVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResidentialQualificationEligibility(
    ResidentialQualificationEligibilityVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
