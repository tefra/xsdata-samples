from dataclasses import dataclass
from .mode_of_operation_value_structure import ModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ModeOfOperation1(ModeOfOperationValueStructure):
    class Meta:
        name = "ModeOfOperation"
        namespace = "http://www.netex.org.uk/netex"
