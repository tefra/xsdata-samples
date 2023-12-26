from dataclasses import dataclass
from .check_constraint_delay_version_structure import (
    CheckConstraintDelayVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintDelay(CheckConstraintDelayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
