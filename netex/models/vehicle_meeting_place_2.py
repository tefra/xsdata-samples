from __future__ import annotations

from dataclasses import dataclass

from .addressable_place_version_structure import (
    AddressablePlaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPlace2(AddressablePlaceVersionStructure):
    class Meta:
        name = "VehicleMeetingPlace_"
        namespace = "http://www.netex.org.uk/netex"
