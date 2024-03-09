from dataclasses import dataclass

from .transfer_restriction_ref_structure import TransferRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferRestrictionRef(TransferRestrictionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
