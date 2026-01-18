from __future__ import annotations

from dataclasses import dataclass

from .compound_train_ref_structure import CompoundTrainRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompoundTrainRef(CompoundTrainRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
