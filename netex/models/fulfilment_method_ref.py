from __future__ import annotations

from dataclasses import dataclass

from .fulfilment_method_ref_structure import FulfilmentMethodRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FulfilmentMethodRef(FulfilmentMethodRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
