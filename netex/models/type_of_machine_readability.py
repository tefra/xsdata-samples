from __future__ import annotations

from dataclasses import dataclass

from .type_of_machine_readability_version_structure import (
    TypeOfMachineReadabilityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfMachineReadability(TypeOfMachineReadabilityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
