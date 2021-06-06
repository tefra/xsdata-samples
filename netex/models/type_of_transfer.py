from dataclasses import dataclass
from .type_of_transfer_value_structure import TypeOfTransferValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfTransfer(TypeOfTransferValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
