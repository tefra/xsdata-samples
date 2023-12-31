from dataclasses import dataclass, field
from typing import Optional
from .type_of_machine_readability_ref import TypeOfMachineReadabilityRef
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfMediumAccessDeviceValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfMediumAccessDevice_ValueStructure"

    type_of_machine_readability_ref: Optional[
        TypeOfMachineReadabilityRef
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfMachineReadabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
