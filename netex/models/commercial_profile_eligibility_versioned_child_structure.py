from __future__ import annotations

from dataclasses import dataclass, field

from .commercial_profile_ref import CommercialProfileRef
from .customer_eligibility_versioned_child_structure import (
    CustomerEligibilityVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommercialProfileEligibilityVersionedChildStructure(
    CustomerEligibilityVersionedChildStructure
):
    class Meta:
        name = "CommercialProfileEligibility_VersionedChildStructure"

    commercial_profile_ref: None | CommercialProfileRef = field(
        default=None,
        metadata={
            "name": "CommercialProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
