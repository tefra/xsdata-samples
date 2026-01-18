from __future__ import annotations

from dataclasses import dataclass

from .transport_type_ref_structure import TransportTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeRefStructure(TransportTypeRefStructure):
    pass
