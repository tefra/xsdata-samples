from dataclasses import dataclass
from .check_constraint_throughput_ref_structure import CheckConstraintThroughputRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintThroughputRef(CheckConstraintThroughputRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
