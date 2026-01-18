from __future__ import annotations

from dataclasses import dataclass

from .default_dead_run_run_time_versioned_child_structure import (
    DefaultDeadRunRunTimeVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultDeadRunRunTime(DefaultDeadRunRunTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
