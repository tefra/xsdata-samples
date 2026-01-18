from __future__ import annotations

from dataclasses import dataclass

from .place_in_sequence_ref_structure import PlaceInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceInSequenceRef(PlaceInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
