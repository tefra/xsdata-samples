from __future__ import annotations

from dataclasses import dataclass

from .cycle_model_profile_ref_structure import CycleModelProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CycleModelProfileRef(CycleModelProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
