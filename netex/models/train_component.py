from __future__ import annotations

from dataclasses import dataclass

from .train_component_version_structure import TrainComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponent(TrainComponentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
