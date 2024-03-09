from dataclasses import dataclass

from .dead_run_ref_structure import DeadRunRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeadRunRef(DeadRunRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
