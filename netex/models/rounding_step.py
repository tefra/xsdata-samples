from __future__ import annotations

from dataclasses import dataclass

from .rounding_step_versioned_child_structure import (
    RoundingStepVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoundingStep(RoundingStepVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
