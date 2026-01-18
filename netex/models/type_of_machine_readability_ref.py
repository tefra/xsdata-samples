from __future__ import annotations

from dataclasses import dataclass

from .type_of_machine_readability_ref_structure import (
    TypeOfMachineReadabilityRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfMachineReadabilityRef(TypeOfMachineReadabilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
