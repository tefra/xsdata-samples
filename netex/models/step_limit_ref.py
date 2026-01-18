from __future__ import annotations

from dataclasses import dataclass

from .step_limit_ref_structure import StepLimitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StepLimitRef(StepLimitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
