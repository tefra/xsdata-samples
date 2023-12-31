from dataclasses import dataclass
from .flexible_mode_of_operation_ref_structure import (
    FlexibleModeOfOperationRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleModeOfOperationRef(FlexibleModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
