from dataclasses import dataclass
from .check_constraint_delay_ref_structure import (
    CheckConstraintDelayRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintDelayRef(CheckConstraintDelayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
