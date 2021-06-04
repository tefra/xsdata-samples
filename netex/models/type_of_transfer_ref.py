from dataclasses import dataclass
from netex.models.type_of_transfer_ref_structure import TypeOfTransferRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfTransferRef(TypeOfTransferRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
