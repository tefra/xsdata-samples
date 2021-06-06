from dataclasses import dataclass
from .transferability_ref_structure import TransferabilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferabilityRef(TransferabilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
