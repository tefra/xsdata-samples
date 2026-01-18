from __future__ import annotations

from dataclasses import dataclass

from .fare_element_in_sequence_ref_structure import (
    FareElementInSequenceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareElementInSequenceRef(FareElementInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
