from __future__ import annotations

from dataclasses import dataclass

from .train_element_ref_structure import TrainElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainElementRef(TrainElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
