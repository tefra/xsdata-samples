from __future__ import annotations

from dataclasses import dataclass

from .type_of_transfer_ref_structure import TypeOfTransferRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfTransferRef(TypeOfTransferRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
