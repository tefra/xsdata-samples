from __future__ import annotations

from dataclasses import dataclass

from .compound_train_version_structure import CompoundTrainVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompoundTrain(CompoundTrainVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
