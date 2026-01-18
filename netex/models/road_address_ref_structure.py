from __future__ import annotations

from dataclasses import dataclass

from .address_ref_structure import AddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoadAddressRefStructure(AddressRefStructure):
    pass
