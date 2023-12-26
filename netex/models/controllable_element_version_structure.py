from dataclasses import dataclass, field
from typing import Optional
from .access_right_parameter_assignments_rel_structure import (
    AccessRightParameterAssignmentsRelStructure,
)
from .cell_versioned_child_structure import PriceableObjectVersionStructure
from .controllable_element_prices_rel_structure import (
    ControllableElementPricesRelStructure,
)
from .controllable_elements_in_sequence_rel_structure import (
    ControllableElementsInSequenceRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControllableElementVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "ControllableElement_VersionStructure"

    access_right_parameter_assignments: Optional[
        AccessRightParameterAssignmentsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "accessRightParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    controllable_elements_in_sequence: Optional[
        ControllableElementsInSequenceRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "controllableElementsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[ControllableElementPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
