from __future__ import annotations

from dataclasses import dataclass

from .train_component_ref_structure import TrainComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentRef(TrainComponentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
