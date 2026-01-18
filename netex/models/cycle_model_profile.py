from __future__ import annotations

from dataclasses import dataclass

from .cycle_model_profile_version_structure import (
    CycleModelProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CycleModelProfile(CycleModelProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
