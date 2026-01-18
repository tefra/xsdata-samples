from __future__ import annotations

from dataclasses import dataclass

from .dead_run_with_calls_version_structure import (
    DeadRunWithCallsVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeadRun(DeadRunWithCallsVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
