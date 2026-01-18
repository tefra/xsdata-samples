from __future__ import annotations

from dataclasses import dataclass

from .parking_properties_ref_structure import ParkingPropertiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPropertiesRef(ParkingPropertiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
