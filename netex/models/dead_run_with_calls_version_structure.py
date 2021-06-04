from dataclasses import dataclass, field
from typing import Optional
from netex.models.dead_run_calls_rel_structure import DeadRunCallsRelStructure
from netex.models.dead_run_version_structure import DeadRunVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeadRunWithCallsVersionStructure(DeadRunVersionStructure):
    class Meta:
        name = "DeadRunWithCalls_VersionStructure"

    calls: Optional[DeadRunCallsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
