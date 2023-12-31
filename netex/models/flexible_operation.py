from dataclasses import dataclass
from .flexible_mode_of_operation_value_structure import (
    FlexibleModeOfOperationValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleOperation(FlexibleModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
