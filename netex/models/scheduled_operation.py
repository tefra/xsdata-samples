from dataclasses import dataclass

from .scheduled_mode_of_operation_value_structure import (
    ScheduledModeOfOperationValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduledOperation(ScheduledModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
