from dataclasses import dataclass, field
from typing import Optional

from .submodes_rel_structure import SubmodesRelStructure
from .type_of_mode_of_operation_ref import TypeOfModeOfOperationRef
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ModeOfOperationValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "ModeOfOperation_ValueStructure"

    type_of_mode_of_operation_ref: Optional[TypeOfModeOfOperationRef] = field(
        default=None,
        metadata={
            "name": "TypeOfModeOfOperationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    submodes: Optional[SubmodesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
