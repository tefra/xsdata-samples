from __future__ import annotations

from dataclasses import dataclass

from .passing_time_versioned_child_structure import (
    PassingTimeVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassingTime(PassingTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
