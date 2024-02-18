from dataclasses import dataclass
from .mode_of_operation_ref_structure import ModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ModeOfOperationRef(ModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
