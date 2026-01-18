from __future__ import annotations

from dataclasses import dataclass

from .train_ref_structure import TrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainRef(TrainRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
