from __future__ import annotations

from dataclasses import dataclass

from .onboard_stay_versioned_chlld_structure import (
    OnboardStayVersionedChlldStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnboardStay(OnboardStayVersionedChlldStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
