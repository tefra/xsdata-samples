from dataclasses import dataclass

from .check_constraint_throughput_version_structure import (
    CheckConstraintThroughputVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintThroughput(CheckConstraintThroughputVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
