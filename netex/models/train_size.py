from __future__ import annotations

from dataclasses import dataclass

from .train_size_structure import TrainSizeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainSize(TrainSizeStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
