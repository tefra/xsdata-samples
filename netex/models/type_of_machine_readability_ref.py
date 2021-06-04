from dataclasses import dataclass
from netex.models.type_of_machine_readability_ref_structure import TypeOfMachineReadabilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfMachineReadabilityRef(TypeOfMachineReadabilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
