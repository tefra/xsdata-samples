from dataclasses import dataclass

from .alternative_mode_of_operation_value_structure import (
    AlternativeModeOfOperationValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AlternativeModeOfOperation1(AlternativeModeOfOperationValueStructure):
    class Meta:
        name = "AlternativeModeOfOperation"
        namespace = "http://www.netex.org.uk/netex"
