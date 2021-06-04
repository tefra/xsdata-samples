from dataclasses import dataclass
from netex.models.transfer_duration_structure import TransferDurationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferDuration(TransferDurationStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
