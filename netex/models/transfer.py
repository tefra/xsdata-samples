from dataclasses import dataclass
from netex.models.transfer_version_structure import TransferVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Transfer(TransferVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
