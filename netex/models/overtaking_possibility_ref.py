from __future__ import annotations

from dataclasses import dataclass

from .overtaking_possibility_ref_structure import (
    OvertakingPossibilityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OvertakingPossibilityRef(OvertakingPossibilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
