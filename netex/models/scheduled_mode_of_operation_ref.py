from dataclasses import dataclass

from .scheduled_mode_of_operation_ref_structure import (
    ScheduledModeOfOperationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduledModeOfOperationRef(ScheduledModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
