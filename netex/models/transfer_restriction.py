from dataclasses import dataclass
from netex.models.transfer_restriction_version_structure import TransferRestrictionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferRestriction(TransferRestrictionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
