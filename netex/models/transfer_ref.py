from dataclasses import dataclass
from netex.models.transfer_ref_structure import TransferRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferRef(TransferRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
