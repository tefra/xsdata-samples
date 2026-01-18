from __future__ import annotations

from dataclasses import dataclass

from .accommodation_ref_structure import AccommodationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccommodationRef(AccommodationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
